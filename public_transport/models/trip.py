from django.db import models
from public_transport.models import Route


class Trip(models.Model):
    route_id = models.ForeignKey(Route, on_delete=models.CASCADE)
    service_id = models.PositiveIntegerField()
    trip_id = models.CharField(primary_key=True, max_length=20)
    headsign = models.CharField(max_length=50)
    direction_id = models.PositiveIntegerField()

    def __str__(self):
        return f'trip id: {self.trip_id}, route_id: {self.route_id}, headsign: {self.headsign}'
