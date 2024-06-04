from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model

from ..signals import account_activation_token
from ..exceptions import VerificationFailedException


User = get_user_model()

class VerifyEmailConfirmView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
            
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({
                "status_code": 200,
                "detail": "success"
            })
        else:
            raise VerificationFailedException

