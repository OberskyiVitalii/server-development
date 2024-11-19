from django.urls import path
from tickets.views import TicketsList, TicketsDetail

urlpatterns = [
    path('api/v1/tickets/', TicketsList.as_view(), name='tickets_list'),
    path('api/v1/ticket/<int:pk>/', TicketsDetail.as_view(), name='ticket_detail'),
]
