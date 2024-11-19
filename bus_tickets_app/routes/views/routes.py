from rest_framework import generics
from routes.models import Routes
from routes.serializers import RoutesSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(tags=['Routes'])
class RoutesList(generics.ListCreateAPIView):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer

    @extend_schema(description="Fetch all available routes.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description="Create a new route.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

@extend_schema(tags=['Routes'])
class RoutesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Routes.objects.all()
    serializer_class = RoutesSerializer

    @extend_schema(description="Retrieve a route by its ID.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description="Update an existing route by its ID.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @extend_schema(description="Update an existing route by its ID.")
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(description="Delete a route by its ID.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
