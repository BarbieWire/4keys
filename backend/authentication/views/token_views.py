from rest_framework_simplejwt.views import TokenRefreshView

from core.settings import settings

from ..serializers import CookieTokenRefreshSerializer


class CookieRefreshTokenView(TokenRefreshView):
    serializer_class = CookieTokenRefreshSerializer

    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            response.set_cookie(
                **settings.SIMPLE_JWT_COOKIE_PROPERTIES,
                value=response.data['access'],
                key=settings.SIMPLE_JWT['AUTH_COOKIE']
            )
            response.set_cookie(
                **settings.SIMPLE_JWT_COOKIE_PROPERTIES,
                value=response.data['refresh'],
                key=settings.SIMPLE_JWT['REFRESH_COOKIE']
            )

            response.data["detail"] = "token has been successfully refreshed"

        return super().finalize_response(request, response, *args, **kwargs)

