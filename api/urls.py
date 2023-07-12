from django.urls import path,include
from .views import *

urlpatterns = [
    path('', RoutesView.as_view()),
    path('system/', ElevatorSystemView.as_view()),
    path('system/<int:system_name>/', ElevatorSystemViewByPk.as_view()),
    path('elevators/', ElevatorView.as_view()),
    path('elevators/<int:elevator_system>/<int:pk>/', ElevatorViewByPk.as_view()),
    path('requests/', ElevatorRequestsView.as_view()),
    path('requests/<int:elevator_system>/<int:pk>/', ElevatorRequestsViewByPk.as_view()),
]