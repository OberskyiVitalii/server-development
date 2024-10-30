from django.db import models

from routes.models import Routes
from customers.models import Customers

class Tickets(models.Model):
    route_id = models.ForeignKey(Routes, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    seat = models.IntegerField()
    status = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return f'{self.seat} - {self.price}'