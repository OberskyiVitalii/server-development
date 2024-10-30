from django.db import models

class Drivers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'