from rest_framework import viewsets
from public_transport.models import Stop
from public_transport.serializers import StopSerializer


class StopViewSet(viewsets.ModelViewSet):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer
