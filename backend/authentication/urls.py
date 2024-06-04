from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView

from .views import (
    # token cookie logic
    SignUpView,
    SignInView,
    LogoutView,
    # user
    UserViewSet,
    ChangePassword,
    # cookies
    CookieRefreshTokenView,
    #verifications
    VerifyEmailConfirmView
)


urlpatterns = [
    # obtain tokens
    # view classes are declared in simpleJWT module
    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', CookieRefreshTokenView.as_view(), name="token_refresh"),
    # retrieve user
    path('user/', UserViewSet.as_view({'get': 'retrieve'}), name="retrieve_user"),
    # login / logout / register views
    path('register/', SignUpView.as_view(), name='auth_register'),
    path('login/', SignInView.as_view(), name="auth_login"),
    path('logout/', LogoutView.as_view(), name="auth_logout"),
    
    path('change-password/', ChangePassword.as_view(), name='change_password'), 
    path('reset-password/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    path('verify-email-confirm/<uidb64>/<token>/', VerifyEmailConfirmView.as_view(), name='verify-email-confirm'),
]
