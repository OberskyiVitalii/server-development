from rest_framework import serializers

from routes.models import Routes
from busses.serializers.busses import BussesSerializer

class RoutesSerializer(serializers.ModelSerializer):
    bus = BussesSerializer()
    
    class Meta:
        model = Routes
        fields = ['id', 'departure_location', 'destination', 'travel_time', 'distance', 'bus', 'number_of_available_seats']