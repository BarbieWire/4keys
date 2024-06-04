from rest_framework import serializers
from ..models import UserModified


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModified
        fields = (
            'email',
            'is_active',
        )


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
