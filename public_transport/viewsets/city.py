from rest_framework import viewsets
from public_transport.models import City
from public_transport.serializers.city import CitySerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
