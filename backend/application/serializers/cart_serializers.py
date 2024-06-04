from application.models import *
from rest_framework import serializers

from .product_serializers import ProductSerializer


class CartItemsSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField("get_product")
    total = serializers.SerializerMethodField("get_total_price")

    def get_total_price(self, obj):
        return obj.qty * Product.objects.get(id=obj.product_id.id).price

    def get_product(self, obj):
        instance = Product.objects.get(id=obj.product_id.id)
        return ProductSerializer(instance=instance).data

    class Meta:
        model = CartItem
        fields = (
            'id',
            'qty',
            'product',
            'total',
        )


class UserCartItemsAddSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(default=True)

    class Meta:
        model = CartItem
        fields = (
            'status',
            'qty',
            'cart_id',
            'product_id'
        )
