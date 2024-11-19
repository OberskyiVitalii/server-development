from rest_framework import generics
from drf_spectacular.utils import extend_schema

from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer

@extend_schema(tags=['Schedule'])
class ScheduleList(generics.ListCreateAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    @extend_schema(description="Fetch all available schedules.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description="Create a new schedule.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

@extend_schema(tags=['Schedule'])
class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    @extend_schema(description="Retrieve a schedule by its ID.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(description="Update an existing schedule by its ID.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    @extend_schema(description="Update an existing schedule by its ID.")
    def patch(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @extend_schema(description="Delete a schedule by its ID.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
