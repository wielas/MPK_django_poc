from rest_framework import viewsets
from public_transport.models import StopTimes
from public_transport.serializers import StopTimesSerializer


class StopTimesViewSet(viewsets.ModelViewSet):
    queryset = StopTimes.objects.all()
    serializer_class = StopTimesSerializer
