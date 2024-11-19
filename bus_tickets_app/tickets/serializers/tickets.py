from rest_framework import serializers

from tickets.models import Tickets
from routes.models import Routes
from customers.models import Customers

class TicketsSerializer(serializers.ModelSerializer):
    route = serializers.PrimaryKeyRelatedField(queryset=Routes.objects.all(), required=True)
    customer = serializers.PrimaryKeyRelatedField(queryset=Customers.objects.all(), required=True)
    
    class Meta:
        model = Tickets
        fields = ['id', 'route', 'customer', 'seat', 'status', 'price']