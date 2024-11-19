from rest_framework import serializers

from tickets.models import Tickets
from routes.serializers.routes import RoutesSerializer
from customers.serializers.customers import CustomersSerializer

class TicketsSerializer(serializers.ModelSerializer):
    route = RoutesSerializer()
    customer = CustomersSerializer()
    
    class Meta:
        model = Tickets
        fields = ['id', 'route', 'customer', 'seat', 'status', 'price']