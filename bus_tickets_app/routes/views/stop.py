from rest_framework import generics
from drf_spectacular.utils import extend_schema

from routes.models import Stop
from routes.serializers import StopSerializer

@extend_schema(tags=['Routes'])
class StopList(generics.ListCreateAPIView):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer

    @extend_schema(description="Fetch all available stops.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description="Create a new stop.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

@extend_schema(tags=['Routes'])
class StopDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stop.objects.all()
    serializer_class = StopSerializer

    @extend_schema(description="Retrieve a stop by its ID.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description="Update an existing stop by its ID.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @extend_schema(description="Update an existing stop by its ID.")
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(description="Delete a stop by its ID.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

@extend_schema(tags=['Routes'], description="Retrieve a stops by routes ID.")
class StopsByRoute(generics.ListAPIView):
    serializer_class = StopSerializer

    def get_queryset(self):
        route_id = self.kwargs['route_id']
        return Stop.objects.filter(route_id=route_id)