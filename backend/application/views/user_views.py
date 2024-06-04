# rest framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions

# vanila django
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

# custom Exceptions
from ..exceptions import *

# models + serializers
from ..models import *
from ..serializers import (
    CartItemsSerializer,
    WishlistItemsSerializer,
    UserCartItemsAddSerializer,

    ProductSerializer,
)


class UserCartItemsViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartItemsSerializer

    @staticmethod
    def create_cart(request):
        return Cart.objects.create(user_id=request.user)

    def get_request_data(self, request, item_id):
        item = get_object_or_404(Product, id=item_id)
        try:
            return item, Cart.objects.get(user_id=request.user)
        except ObjectDoesNotExist:
            return item, self.create_cart(request)

    def destroy(self, request, *args, **kwargs):
        item, cart = self.get_request_data(request, kwargs["pk"])

        data = WishlistItem.objects.get(product_id=item, wishlist_id__user_id=request.user)
        data.in_cart = False
        data.save()

        try:
            instance = CartItem.objects.get(product_id=item, cart_id=cart)
            instance.delete()
            serializer = ProductSerializer(instance=item, many=False)
            return Response(serializer.data)

        except ObjectDoesNotExist:
            raise Http404

    def create(self, request, *args, **kwargs):
        item, cart = self.get_request_data(request, request.data["pk"])
        if CartItem.objects.filter(product_id=item, cart_id=cart):
            raise ObjectAlreadyExists

        try:
            data = WishlistItem.objects.get(product_id=item, wishlist_id__user_id=request.user)
            data.in_cart = True
            data.save()
        except ObjectDoesNotExist:
            pass

        data = CartItem.objects.create(cart_id=cart, product_id=item)
        serializer = UserCartItemsAddSerializer(instance=data, many=False)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        item, cart = self.get_request_data(request, kwargs["pk"])
        data = CartItem.objects.get(product_id=item, cart_id=cart)
        data.qty = request.data['qty']
        data.save()

        serializer = CartItemsSerializer(data)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        # cart exists, if not create one
        try:
            Cart.objects.get(user_id=request.user)
        except ObjectDoesNotExist:
            self.create_cart(request=request)

        queryset = CartItem.objects.filter(cart_id__user_id=request.user)

        serializer = CartItemsSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        pass


class UserWishlistItemsViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = WishlistItemsSerializer

    @staticmethod
    def create_wishlist(request):
        return Wishlist.objects.create(user_id=request.user)

    def get_request_data(self, request, item_id):
        item = get_object_or_404(Product, id=item_id)
        try:
            return item, Wishlist.objects.get(user_id=request.user)
        except ObjectDoesNotExist:
            return item, self.create_wishlist(request)

    def destroy(self, request, *args, **kwargs):
        item, wishlist = self.get_request_data(request, kwargs["pk"])
        instance = WishlistItem.objects.get(product_id=item, wishlist_id=wishlist)
        instance.delete()

        serializer = WishlistItemsSerializer(instance=instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        item, wishlist = self.get_request_data(request, request.data["pk"])
        try:
            # impossible to have duplicates in wishlist
            WishlistItem.objects.get(product_id=item, wishlist_id=wishlist)
            raise ObjectAlreadyExists

        except ObjectDoesNotExist:
            try:
                # check if object in users cart, making flag "in_cart" in True statement
                CartItem.objects.get(product_id=item, cart_id__user_id=request.user)
                obj = WishlistItem.objects.create(wishlist_id=wishlist, product_id=item, in_cart=True)
                serializer = WishlistItemsSerializer(obj)
                return Response(serializer.data)

            except ObjectDoesNotExist:
                obj = WishlistItem.objects.create(wishlist_id=wishlist, product_id=item)
                serializer = WishlistItemsSerializer(obj)
                return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        try:
            Wishlist.objects.get(user_id=request.user)
        except ObjectDoesNotExist:
            self.create_wishlist(request=request)

        queryset = WishlistItem.objects.filter(wishlist_id__user_id=request.user)
        serializer = WishlistItemsSerializer(queryset, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        pass