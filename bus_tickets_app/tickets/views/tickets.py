from rest_framework import generics
from drf_spectacular.utils import extend_schema

from tickets.models import Tickets
from tickets.serializers import TicketsSerializer

@extend_schema(tags=['Tickets'])
class TicketsList(generics.ListCreateAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer

    @extend_schema(description="Fetch all available tickets.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description="Create a new ticket.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

@extend_schema(tags=['Tickets'])
class TicketsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializer

    @extend_schema(description="Retrieve a ticket by its ID.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description="Update an existing ticket by its ID.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @extend_schema(description="Update an existing ticket by its ID.")
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(description="Delete a ticket by its ID.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
