from django.shortcuts import render
from .serializers import TruckSerializer, UserzSerializer
from rest_framework import viewsets      
from .models import Truck, Userz               

class TruckView(viewsets.ModelViewSet):  
    serializer_class = TruckSerializer   
    queryset = Truck.objects.all()   

class UserzView(viewsets.ModelViewSet):  
    serializer_class = UserzSerializer   
    queryset = Userz.objects.all()   