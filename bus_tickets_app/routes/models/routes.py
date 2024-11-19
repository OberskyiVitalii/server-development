from django.db import models

class Routes(models.Model):
    departure_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    distance = models.FloatField()
    bus = models.ForeignKey('busses.Busses', on_delete=models.SET_NULL, null=True)
    number_of_available_seats = models.IntegerField()

    def __str__(self):
        return f'{self.departure_location} - {self.destination}'