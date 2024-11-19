from django.db import models

class Busses(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    number_plate = models.CharField(max_length=10)
    driver = models.ForeignKey('drivers.Drivers', on_delete=models.SET_NULL, null=True, related_name='drivers')
    number_of_seats = models.IntegerField()
    route = models.ForeignKey('routes.Routes', on_delete=models.SET_NULL, null=True, related_name='routes')
    status = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.brand} {self.brand} {self.number_plate}'