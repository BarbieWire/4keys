from rest_framework import serializers
from ..models import Banner

class BannerSerizalizer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"