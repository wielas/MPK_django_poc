from rest_framework import serializers
from public_transport.models import Stop


class StopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stop
        fields = ['id', 'code', 'name', 'longitude', 'latitude']
