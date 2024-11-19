from rest_framework import serializers

from schedule.models import Schedule
from routes.serializers.routes import RoutesSerializer

class ScheduleSerializer(serializers.ModelSerializer):
    route = RoutesSerializer()
    
    class Meta:
        model = Schedule
        fields = ['id', 'route', 'departure_time', 'arrival_time', 'status']