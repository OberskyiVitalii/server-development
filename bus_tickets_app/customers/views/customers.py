from rest_framework import generics
from drf_spectacular.utils import extend_schema

from customers.models import Customers
from customers.serializers import CustomersSerializer

@extend_schema(tags=['Customers'])
class CustomersList(generics.ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

    @extend_schema(description="Fetch all available customers.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description="Create a new customer.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

@extend_schema(tags=['Customers'])
class CustomersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer

    @extend_schema(description="Retrieve a customer by their ID.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description="Update an existing customer by their ID.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(description="Update an existing customer by its ID.")
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(description="Delete a customer by their ID.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
