from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView

from rest_framework.exceptions import ValidationError

from django.contrib.auth import authenticate
from core.settings import settings

from ..serializers import (
    RegisterSerializer, 
    LoginSerializer,
)

from ..exceptions import *
from ..models import UserModified


class SignUpView(CreateAPIView):
    """
    Allows to crete a new instance on User if based on validation
    described in RegisterSerializer (register)
    """
    queryset = UserModified.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class SignInView(APIView):
    """
    Allows user to obtain a pair of tokens as
    HTTPOnly secured cookies (login)
    set JWT as cookies
    """

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        response = Response()
        serializer = self.serializer_class(data=request.data)
        
        if not request.user.is_anonymous:
            raise AlreadySignedInException
    
        if not serializer.is_valid():
            raise ValidationError(serializer.errors)
        
        user = authenticate(
            email=request.data.get('email', None), 
            password=request.data.get('password', None)
        )

        # response object
        tokens = user.get_tokens()  # return a standart python dict of keys 
        for token_name, value in tokens.items():
            response.set_cookie(
                **settings.SIMPLE_JWT_COOKIE_PROPERTIES,
                value=value,
                key=token_name
            )

        response.data = {
            "detail": "Successfully logged in",
            "user": self.serializer_class(user).data
        }
        return response
    
    def cookies_exist(self, request, *args, **kwargs):
        return (
            request.COOKIES.get(settings.SIMPLE_JWT["REFRESH_COOKIE"], None), 
            request.COOKIES.get(settings.SIMPLE_JWT["AUTH_COOKIE"], None)
        )
 

class LogoutView(APIView):
    """
    logging out from system
    Expects at least 'access_token'
    """
    permission_classes = [IsAuthenticated]

    refresh_key = settings.SIMPLE_JWT["REFRESH_COOKIE"]
    access_key = settings.SIMPLE_JWT["AUTH_COOKIE"]

    def post(self, request, *args, **kwargs):
        response = Response()

        response.delete_cookie(key=self.access_key, samesite="None")
        if request.COOKIES[self.refresh_key]:
            response.delete_cookie(key=self.refresh_key, samesite="None")

        response.data = {
            "detail": "Successfully logged out",
            "status_code": 200
        }
        return response
