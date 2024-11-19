from django.urls import path
from drivers.views import DriversList, DriversDetail

urlpatterns = [
    path('api/v1/drivers/', DriversList.as_view(), name='drivers_list'),
    path('api/v1/driver/<int:pk>/', DriversDetail.as_view(), name='driver_detail'),
]
