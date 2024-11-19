from rest_framework import serializers

from routes.models import Routes
from busses.models import Busses

class RoutesSerializer(serializers.ModelSerializer):
    bus = serializers.PrimaryKeyRelatedField(queryset=Busses.objects.all(), required=False)

    class Meta:
        model = Routes
        fields = ['id', 'departure_location', 'destination', 'distance', 'bus', 'number_of_available_seats']