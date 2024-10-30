from django.db import models

from routes.models import Routes

class Stop(models.Model):
    city = models.CharField(max_length=255)
    route_id = models.ForeignKey(Routes, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.city}'
    
