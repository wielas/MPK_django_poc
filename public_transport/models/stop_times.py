from django.db import models
from public_transport.models import Stop, Trip


class StopTimes(models.Model):
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
    departure_time = models.TimeField()
    stop_id = models.ForeignKey(Stop, on_delete=models.CASCADE)

    def __str__(self):
        return f'stop_id: {self.stop_id} depart: {self.departure_time}'
