from rest_framework import serializers

from routes.models import Stop
from routes.models import Routes

class StopSerializer(serializers.ModelSerializer):
    route = serializers.PrimaryKeyRelatedField(queryset=Routes.objects.all(), required=False)
    
    class Meta:
        model = Stop
        fields = ['id', 'city', 'route']