from django.urls import path
from .api_views import (
    EventListCreateAPI,
    EventDetailAPI,
    RegisterEventAPI
)

urlpatterns = [
    path('events/', EventListCreateAPI.as_view()),
    path('events/<int:pk>/', EventDetailAPI.as_view()),
    path('register/', RegisterEventAPI.as_view()),
]
