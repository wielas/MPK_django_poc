from rest_framework import serializers
from public_transport.models import Trip


class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trip
        fields = ['route_id', 'service_id', 'trip_id', 'direction_id']
