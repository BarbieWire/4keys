from rest_framework import generics
from rest_framework.response import Response

from ..serializers import BannerSerizalizer
from ..models import Banner


class BannerView(generics.ListAPIView):
    serializer_class = BannerSerizalizer
    queryset = Banner.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    