from rest_framework import serializers

from busses.models import Busses
from drivers.serializers.drivers import DriversSerializer
from routes.serializers.routes import RoutesSerializer

class BussesSerializer(serializers.ModelSerializer):
    driver = DriversSerializer()
    route = RoutesSerializer()
    
    class Meta:
        model = Busses
        fields = ['id', 'brand', 'model', 'year', 'number_plate', 'driver', 'route', 'status', 'number_of_seats']