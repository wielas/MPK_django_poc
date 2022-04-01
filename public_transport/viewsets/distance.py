from rest_framework import viewsets
from rest_framework.response import Response

from public_transport.models import Stop
from public_transport.serializers import StopSerializer


class DistanceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that calculates the distance from given coordinates
    """
    queryset = Stop.objects.all()
    serializer_class = StopSerializer

    # def get_queryset(self):
    #     return self.queryset.filter(name="Grabowa")


    def update(self, request, *args, **kwargs):
        print(request.data)