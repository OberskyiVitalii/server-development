from django.db import models

class Busses(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    number_plate = models.CharField(max_length=10)
    driver_id = models.CharField(max_length=50)
    number_of_seats = models.IntegerField()
    route_id = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return f'{self.brand} {self.brand} {self.number_plate}'