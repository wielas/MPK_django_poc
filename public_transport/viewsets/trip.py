from rest_framework import viewsets
from public_transport.models import Trip
from public_transport.serializers import TripSerializer


class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
