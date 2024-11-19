from django.urls import path
from routes.views import RoutesList, RoutesDetail
from routes.views import StopList, StopDetail, StopsByRoute

urlpatterns = [
    path('api/v1/routes/', RoutesList.as_view(), name='routes_list'),
    path('api/v1/stop/', StopList.as_view(), name='stop_list'),
    path('api/v1/route/<int:pk>/', RoutesDetail.as_view(), name='route_detail'),
    path('api/v1/stop/<int:pk>/', StopDetail.as_view(), name='stop_detail'),
    path('api/v1/stops_by_route/<int:route_id>/', StopsByRoute.as_view(), name='stops_by_route'),
]
