from .authentication_views import SignInView, SignUpView, LogoutView
from .user_views import UserViewSet, ChangePassword
from .token_views import CookieRefreshTokenView

from .verify_views import VerifyEmailConfirmView