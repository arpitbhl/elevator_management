from django.urls import path,include
from .views import *

urlpatterns = [
    path('<int:elevator_system>/<int:pk>/', ElevatorView.as_view()),
]