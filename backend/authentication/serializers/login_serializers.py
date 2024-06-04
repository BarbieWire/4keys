from rest_framework import serializers
from ..models import UserModified
from django.contrib.auth import authenticate

from ..exceptions import *


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    
    def validate(self, attrs):
        if not UserModified.objects.filter(email=attrs["email"]):
            raise UserDoesNotExistException
        
        user = authenticate(email=attrs["email"], password=attrs["password"])
        if user is None:
            raise InvalidCredentialsProvidedException

        if not user.is_active:
            raise AccountDeactivatedException

        return attrs

    class Meta:
        model = UserModified
        fields = ("email", "password")