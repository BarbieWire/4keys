from application.models import *
from rest_framework.serializers import ModelSerializer


class RecursiveSerializer(ModelSerializer):
    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CategorySerializer(ModelSerializer):
    children = RecursiveSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'children')
