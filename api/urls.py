from django.urls import path
from .views import *

urlpatterns = [
    path('team/', Team.as_view()),
    path('activity/', Activityview.as_view()),
    path('activity/<int:pk>/', ActivityDetails.as_view()),
    path('contact/', Contactview.as_view()),
]