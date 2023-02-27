
from rest_framework import generics
from .serializer import TeamSerializer, ActivitySerializer, ContactSerializer
from .models import *

class Team(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class Activityview(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer    
 
class ActivityDetails(generics.RetrieveAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer   
    lookup_field = 'pk'

class Contactview(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer