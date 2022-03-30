from django.db import models
from public_transport.models import Stop, Trip


class StopTimes(models.Model):
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    stop_id = models.ForeignKey(Stop, on_delete=models.CASCADE)
    stop_sequence = models.PositiveIntegerField()
    pickup_type = models.PositiveIntegerField()
    drop_off_time = models.PositiveIntegerField()

    def __str__(self):
        return f'trip id: {self.trip_id}, stop_id: {self.stop_id}\n' \
               f'arrive: {self.arrival_time}, depart: {self.departure_time}'
