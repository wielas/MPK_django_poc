from rest_framework import serializers
from public_transport.models import Route


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'short_name', 'description']
