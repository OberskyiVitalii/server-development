from django.urls import path
from schedule.views import ScheduleList, ScheduleDetail

urlpatterns = [
    path('api/v1/schedule/', ScheduleList.as_view(), name='schedule_list'),
    path('api/v1/schedule/<int:pk>/', ScheduleDetail.as_view(), name='schedule_detail'),
]
