from rest_framework import serializers

from drivers.models import Drivers

class DriversSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivers
        fields = ['id', 'first_name', 'last_name', 'phone', 'email']