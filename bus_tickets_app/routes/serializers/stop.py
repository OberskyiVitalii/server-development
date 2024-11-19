from rest_framework import serializers

from routes.models import Stop
from routes.serializers.routes import RoutesSerializer

class StopSerializer(serializers.ModelSerializer):
    route = RoutesSerializer()
    
    class Meta:
        model = Stop
        fields = ['id', 'city', 'route']