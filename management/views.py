from django.shortcuts import render
from .serializers import TruckSerializer 
from rest_framework import viewsets      
from .models import Truck                 

class TruckView(viewsets.ModelViewSet):  
    serializer_class = TruckSerializer   
    queryset = Truck.objects.all()   
