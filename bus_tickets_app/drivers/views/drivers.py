from rest_framework import generics
from drf_spectacular.utils import extend_schema

from drivers.models import Drivers
from drivers.serializers import DriversSerializer

@extend_schema(tags=['Drivers'])
class DriversList(generics.ListCreateAPIView):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer

    @extend_schema(description="Fetch all available drivers.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description="Create a new driver.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

@extend_schema(tags=['Drivers'])
class DriversDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drivers.objects.all()
    serializer_class = DriversSerializer

    @extend_schema(description="Retrieve a driver by their ID.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description="Update an existing driver by their ID.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @extend_schema(description="Update an existing driver by its ID.")
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(description="Delete a driver by their ID.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
