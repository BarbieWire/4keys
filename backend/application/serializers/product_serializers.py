from application.models import *

from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import SerializerMethodField

from application.models import ProductPicture


class ProductGetterMixin:
    def get_brand(self, obj):
        return obj.brand.name

    def get_category(self, obj):
        return obj.category.name


class ProductPictureSerializer(ModelSerializer):
    class Meta:
        model = ProductPicture
        fields = ("id", "picture")


class ProductAttributeValueSeriazlizer(ModelSerializer):
    attribute_name = SerializerMethodField("get_attribute_name")

    def get_attribute_name(self, obj):
        return obj.attribute.name
        
    class Meta:
        model = ProductAttributeValue
        fields = ("value", "attribute_name")


class ProductListSerializer(ModelSerializer, ProductGetterMixin):
    # methods described in productMixin.ProductMixin class
    category = SerializerMethodField('get_category')
    brand = SerializerMethodField("get_brand")
    cover = SerializerMethodField("get_picture")

    def get_picture(self, obj):
        first_picture = obj.pictures.first()
        return ProductPictureSerializer(first_picture, context=self.context).data if first_picture else None
        # always pass the context to the subserializer in order to get everything work fine

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'description',
            'brand',
            'color',
            'normal_price',
            'price_after_discount',
            'stock',
            'vendor_code',
            'cover',
        )


class ProductSerializer(ModelSerializer, ProductGetterMixin):
    # methods described in productMixin.ProductMixin class
    brand = SerializerMethodField("get_brand")
    category = SerializerMethodField('get_category')
    
    pictures = ProductPictureSerializer(many=True, read_only=True)
    # attributes = SerializerMethodField('get_attributes')
    attributes = ProductAttributeValueSeriazlizer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'category',
            'description',
            'brand',
            'color',
            'normal_price',
            'price_after_discount',
            'stock',
            'vendor_code',
            'pictures',
            'attributes',
        )
