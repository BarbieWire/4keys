from rest_framework import serializers
from ..models import UserModified
from rest_framework.validators import UniqueValidator


from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from ..exceptions import *


class PasswordValidator:
    def __call__(self, password):
        try:
            validate_password(password)
        except ValidationError as e:
            errors = list(e)
            raise serializers.ValidationError(errors[0])


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=UserModified.objects.all(),
                message="Please provide a non-registred email address"
            ),
        ],
    )

    password = serializers.CharField(
        write_only=True, 
        required=True, 
        validators=[
            PasswordValidator()
        ]
    )
    repeat_password = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        # password matching validation
        if attrs["password"] != attrs["repeat_password"]:
            raise serializers.ValidationError({"repeat_password": "passwords do not match"})

        return attrs

    def create(self, validated_data):
        user = UserModified.objects.create(email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()

        return user

    class Meta:
        model = UserModified
        fields = ("email", "password", "repeat_password")
