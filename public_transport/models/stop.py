from django.db import models


class Stop(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    code = models.PositiveIntegerField()
    name = models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f'{self.id}, {self.code}, {self.name}'
