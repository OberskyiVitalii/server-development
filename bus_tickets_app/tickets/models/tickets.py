from django.db import models

class Tickets(models.Model):
    route = models.ForeignKey('routes.Routes', on_delete=models.CASCADE, null=False)
    customer = models.ForeignKey('customers.Customers', on_delete=models.CASCADE, null=False)
    seat = models.IntegerField()
    status = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return f'{self.seat} - {self.price}'