from rest_framework import generics
from drf_spectacular.utils import extend_schema

from busses.models import Busses
from busses.serializers import BussesSerializer

@extend_schema(tags=['Busses'])
class BussesList(generics.ListCreateAPIView):
    queryset = Busses.objects.all()
    serializer_class = BussesSerializer

    @extend_schema(description="Fetch all available buses.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description="Create a new bus.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

@extend_schema(tags=['Busses'])
class BussesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Busses.objects.all()
    serializer_class = BussesSerializer

    @extend_schema(description="Retrieve a bus by its ID.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description="Update an existing bus by its ID.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @extend_schema(description="Update an existing bus by its ID.")
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(description="Delete a bus by its ID.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
