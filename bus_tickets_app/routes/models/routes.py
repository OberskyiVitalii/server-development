from django.db import models

from busses.models import Busses

class Routes(models.Model):
    departure_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    travel_time = models.DateTimeField()
    distance = models.FloatField()
    bus_id = models.ForeignKey(Busses, on_delete=models.CASCADE)
    number_of_available_seats = models.IntegerField()

    def __str__(self):
        return f'{self.departure_location} - {self.destination}'