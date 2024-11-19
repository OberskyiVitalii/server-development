from rest_framework import serializers

from schedule.models import Schedule
from routes.models import Routes

class ScheduleSerializer(serializers.ModelSerializer):
    route = serializers.PrimaryKeyRelatedField(queryset=Routes.objects.all(), required=False)
    
    class Meta:
        model = Schedule
        fields = ['id', 'route', 'departure_time', 'arrival_time', 'status']