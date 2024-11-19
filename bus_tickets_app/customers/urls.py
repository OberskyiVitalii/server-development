from django.urls import path
from customers.views import CustomersList, CustomersDetail

urlpatterns = [
    path('api/v1/customers/', CustomersList.as_view(), name='customers_list'),
    path('api/v1/customer/<int:pk>/', CustomersDetail.as_view(), name='customer_detail'),
]
