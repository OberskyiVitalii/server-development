from django.db import models

from routes.models import Routes

class Schedule(models.Model):
    route_id = models.ForeignKey(Routes, on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.departure_time} - {self.arrival_time}'