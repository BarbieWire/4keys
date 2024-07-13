# rest framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import permissions, status

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

import secrets


# class UserCartItemsViewSet(ModelViewSet):
#     serializer_class = CartItemsSerializer
    
#     def generate_session_token(self):
#         return secrets.token_urlsafe(32)

#     def create_cart(self, request):
#         if request.user.is_authenticated:
#             cart, created = Cart.objects.get_or_create(user=request.user)
#         else:
#             session_token = request.session.get('session_token')
#             if not session_token:
#                 session_token = self.generate_session_token()
#                 request.session['session_token'] = session_token
#             cart, created = Cart.objects.get_or_create(session_token=session_token)
#         return cart

#     def get_request_data(self, request, item_id):
#         item = get_object_or_404(Product, id=item_id)
#         try:
#             return item, Cart.objects.get(user_id=request.user)
#         except ObjectDoesNotExist:
#             return item, self.create_cart(request)

#     def destroy(self, request, *args, **kwargs):
#         item, cart = self.get_request_data(request, kwargs["pk"])

#         data = WishlistItem.objects.get(product_id=item, wishlist_id__user_id=request.user)
#         data.in_cart = False
#         data.save()

#         try:
#             instance = CartItem.objects.get(product_id=item, cart_id=cart)
#             instance.delete()
#             serializer = ProductSerializer(instance=item, many=False)
#             return Response(serializer.data)

#         except ObjectDoesNotExist:
#             raise Http404

#     def create(self, request, *args, **kwargs):
#         item, cart = self.get_request_data(request, request.data["pk"])
#         if CartItem.objects.filter(product_id=item, cart_id=cart):
#             raise ObjectAlreadyExists

#         try:
#             data = WishlistItem.objects.get(product_id=item, wishlist_id__user_id=request.user)
#             data.in_cart = True
#             data.save()
#         except ObjectDoesNotExist:
#             pass

#         data = CartItem.objects.create(cart_id=cart, product_id=item)
#         serializer = UserCartItemsAddSerializer(instance=data, many=False)
#         return Response(serializer.data)

#     def update(self, request, *args, **kwargs):
#         item, cart = self.get_request_data(request, kwargs["pk"])
#         data = CartItem.objects.get(product_id=item, cart_id=cart)
#         data.qty = request.data['qty']
#         data.save()

#         serializer = CartItemsSerializer(data)
#         return Response(serializer.data)

#     def list(self, request, *args, **kwargs):
#         # cart exists, if not create one
#         try:
#             Cart.objects.get(user_id=request.user)
#         except ObjectDoesNotExist:
#             self.create_cart(request=request)

#         queryset = CartItem.objects.filter(cart_id__user_id=request.user)

#         serializer = CartItemsSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def get_queryset(self):
#         pass



class CartItemsViewSet(ModelViewSet):
    serializer_class = CartItemsSerializer
    permission_classes = [permissions.AllowAny]
    
    def generate_session_token(self):
        return secrets.token_urlsafe(32)
    
    def __get_cart(self, request):
        self.response = Response()
        if request.user.is_authenticated:
            cart, _ = Cart.objects.get_or_create(user=request.user)
        else:
            session_token = request.COOKIES.get('session_token')
            if not session_token:
                session_token = self.generate_session_token()
                cart, _ = Cart.objects.get_or_create(session_token=session_token)
                self.response.set_cookie('session_token', session_token, httponly=True)
                return cart
            else:
                cart, _ = Cart.objects.get_or_create(session_token=session_token)
                
        return cart
        
    def get_queryset(self):
        cart = self.__get_cart(request=self.request)
        return CartItem.objects.filter(cart=cart)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        self.response.data = serializer.data
        return self.response
    
    def create(self, request, *args, **kwargs):
        cart = self.__get_cart(request=request)
        item = Product.objects.get(id=request.data["id"])
        
        if CartItem.objects.filter(product=item, cart=cart):
            raise ObjectAlreadyExists
        
        CartItem.objects.create(cart=cart, product=item)
        
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        self.response.data = serializer.data
        return self.response
    
    def update(self, request, *args, **kwargs):
        """
        **kwargs (dict):
            - 'pk' (str or int): Primary key to identificate product object.
        """
        id = kwargs["pk"]
        quantity = request.data['qty']
        queryset = self.get_queryset()
        item = queryset.get(id=id)
        item.qty = int(quantity)
        item.save()
        serializer = self.serializer_class(item)
        self.response.data = serializer.data
        return self.response


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