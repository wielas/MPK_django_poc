from rest_framework import serializers
from public_transport.models import Trip


class TripSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trip
        fields = ['route_id', 'service_id', 'trip_id', 'headsign', 'direction_id', 'shape_id', 'brigade_id',
                  'vehicle_id', 'variant_id']
