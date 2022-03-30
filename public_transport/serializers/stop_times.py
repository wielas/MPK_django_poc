from rest_framework import serializers
from public_transport.models import StopTimes


class StopTimesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StopTimes
        fields = ['trip_id', 'arrival_time', 'departure_time', 'stop_id', 'stop_sequence', 'pickup_type',
                  'drop_off_time']
