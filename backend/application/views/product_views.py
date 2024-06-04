from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import mixins

from rest_framework.pagination import PageNumberPagination

# vanila django
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.postgres.search import SearchVector

# custom Exceptions
from ..exceptions import *

# models + serializers
from ..models import *
from ..serializers import (
    ProductListSerializer,
    ProductSerializer,
    CategorySerializer,
)


class ProductsPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'results': data,
            'links': {
               'next_page': self.get_next_link(),
               'previous_page': self.get_previous_link()
            },
            'record_count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
        })


class ProductsViewSet(GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    pagination_class = ProductsPagination

    filtering_fields = ["newness", "popularity"]
    price_fields = ["min", "max"]
    instock_fields = ["instock"]
    query_search_fields = ["q"]

    def get_queryset(self, *args, **kwargs):
        filter_type = self.request.query_params.get('filter')
        search_query = self.request.query_params.get('q')

        properties = self.request.query_params.get('properties', None)

        min_price = self.request.query_params.get('min')
        max_price = self.request.query_params.get('max')
        in_stock = self.request.query_params.get('instock')

        queryset = Product.objects.all()

        if search_query:
            queryset = queryset.annotate(
                search=SearchVector(
                    "category__name", 
                    "name",
                    "description",
                    "brand__name"
                )
            ).filter(search=search_query)

        if properties is not None:
            properties = properties.split(",")
            for attr_value in properties:
                # Filter the queryset to include only products with the specified attribute value
                queryset = queryset.filter(
                    attributes__value=attr_value
                )
            queryset = queryset.distinct()

        if min_price and max_price:
            try:
                min_price, max_price = int(min_price), int(max_price)
            except ValueError:
                raise InvalidPrice

            if min_price < 0 or max_price < 0:
                raise InvalidPriceNegative

            if min_price > max_price:
                raise InvalidPriceMinGreaterThanMax

            queryset = queryset.filter(normal_price__range=[min_price, max_price])

        if in_stock:
            queryset = queryset.filter(stock__gt=0)

        if filter_type:
            match filter_type:
                case "popularity":
                    queryset = queryset.order_by('-views')  
                case "newness":
                    queryset = queryset.order_by('-date_created')
                case _: 
                    raise InvalidFilterType

        return queryset

    def get_serializer_class(self):
        # get method
        if self.action == "list":
            return ProductListSerializer
        # detail view of an object, see more in "get_object" method
        return ProductSerializer

    def get_object(self):
        # called in retrieve method in parent class RetrieveModelMixin
        try:
            return Product.objects.get(vendor_code=self.kwargs["pk"])
        except ObjectDoesNotExist:
            raise Http404

    def list(self, request, *args, **kwargs):
        paginator = self.pagination_class()
        queryset = self.get_queryset(**request.query_params)
        page = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class CategoryViewSet(GenericViewSet, mixins.ListModelMixin):
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(parent=None)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
