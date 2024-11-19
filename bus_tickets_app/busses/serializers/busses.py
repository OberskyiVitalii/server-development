from rest_framework import serializers

from busses.models import Busses
from drivers.models import Drivers
from routes.models import Routes

class BussesSerializer(serializers.ModelSerializer):
    driver = serializers.PrimaryKeyRelatedField(queryset=Drivers.objects.all(), required=False)
    route = serializers.PrimaryKeyRelatedField(queryset=Routes.objects.all(), required=False)
    
    class Meta:
        model = Busses
        fields = ['id', 'brand', 'model', 'year', 'number_plate', 'driver', 'route', 'status', 'number_of_seats']