from django.db import models

class Stop(models.Model):
    city = models.CharField(max_length=255)
    route = models.ForeignKey('routes.Routes', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.city}'
    
