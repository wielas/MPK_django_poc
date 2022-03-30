from django.db import models


class Trip(models.Model):
    # TODO route_id = models.ForeignKey(Route)
    route_id = models.CharField(max_length=10)
    service_id = models.PositiveIntegerField()
    trip_id = models.CharField(primary_key=True, max_length=20)
    headsign = models.CharField(max_length=50)
    direction_id = models.PositiveIntegerField()
    shape_id = models.PositiveIntegerField()
    brigade_id = models.PositiveIntegerField()
    vehicle_id = models.PositiveIntegerField()
    variant_id = models.PositiveIntegerField()

    def __str__(self):
        return f'trip id: {self.trip_id}, route_id: {self.route_id}, headsign: {self.headsign}'
