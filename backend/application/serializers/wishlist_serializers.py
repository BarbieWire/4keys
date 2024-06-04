from application.models import *
from rest_framework import serializers

from .product_serializers import ProductSerializer


class WishlistItemsSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField("get_product")

    def get_product(self, obj):
        instance = Product.objects.get(id=obj.product_id.id)
        return ProductSerializer(instance=instance).data

    class Meta:
        model = WishlistItem
        fields = ('product', 'in_cart')