from django.urls import path, include
from .views import *
from rest_framework import routers

from .views import BannerView


product_router = routers.SimpleRouter()
product_router.register(
    r'products', 
    ProductsViewSet, 
    basename='Product'
)

categories_router = routers.SimpleRouter()
categories_router.register(
    r'categories', 
    CategoryViewSet,
    basename='Categories'
)

wishlist_router = routers.SimpleRouter()
wishlist_router.register(
    r'wishlist', 
    UserWishlistItemsViewSet, 
    basename='WishlistItem'
)

cart_router = routers.SimpleRouter()
cart_router.register(
    r'cart', 
    CartItemsViewSet, 
    basename='CartItem'
)

urlpatterns = [
    path("", include(product_router.urls)),
    path("", include(categories_router.urls)),
    
    path("", include(cart_router.urls)),
    path("", include(wishlist_router.urls)),
    
    path("banners/", BannerView.as_view(), name="banners"),
]
