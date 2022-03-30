from rest_framework import viewsets
from public_transport.models import Route
from public_transport.serializers import RouteSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
