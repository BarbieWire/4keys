from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated

from ..serializers import UserSerializer, ChangePasswordSerializer

from rest_framework.response import Response

from django.contrib.auth import get_user_model

from ..exceptions import PasswordIncorrectException, InvalidCredentialsProvidedException



class UserViewSet(ModelViewSet):
    """
    Allows to obtain credentials of the user
    based on access cookie
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def retrieve(self, request):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        print(request, *args, **kwargs)
        return Response()
    

class ChangePassword(GenericAPIView):
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            raise InvalidCredentialsProvidedException
        
        password = request.data['old_password']
        new_password = request.data['new_password']

        obj = request.user
        if not obj.check_password(raw_password=password):
            raise PasswordIncorrectException
        else:
            obj.set_password(new_password)
            obj.save()
            return Response({'success': 'password changed successfully'}, status=200)
