from django.db import models


class City(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id}, {self.name}'


class Route(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    short_name = models.CharField(max_length=5)
    description = models.TextField()

    def __str__(self):
        return f'{self.id}, {self.short_name}, {self.description}'


class Stop(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    code = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'{self.id}, {self.code}, {self.name}'


class Trip(models.Model):
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
