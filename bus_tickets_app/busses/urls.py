from django.urls import path
from busses.views import BussesList, BussesDetail

urlpatterns = [
    path('api/v1/busses/', BussesList.as_view(), name='busses_list'),
    path('api/v1/bus/<int:pk>/', BussesDetail.as_view(), name='bus_detail'),
]
