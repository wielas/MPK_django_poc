from django.db import models


class Route(models.Model):
    id = models.CharField(primary_key=True, max_length=5)
    short_name = models.CharField(max_length=5)
    description = models.TextField()

    def __str__(self):
        return f'{self.id}, {self.short_name}, {self.description}'
