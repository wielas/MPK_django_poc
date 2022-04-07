from rest_framework import serializers
from public_transport.models import StopTimes
from public_transport.serializers import TripSerializer, StopSerializer


class StopTimesSerializer(serializers.HyperlinkedModelSerializer):
    trip_id = TripSerializer()
    stop_id = StopSerializer()

    class Meta:
        model = StopTimes
        fields = ['trip_id', 'departure_time', 'stop_id']
