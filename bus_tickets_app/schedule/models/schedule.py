from django.db import models

class Schedule(models.Model):
    route = models.ForeignKey('routes.Routes', on_delete=models.SET_NULL, null=True)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    status = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.departure_time} - {self.arrival_time}'