from .serializers import TruckSerializer, UserzSerializer, DriverSerializer
from rest_framework import viewsets      
from .models import Truck, Userz, Driver
from rest_framework.views import APIView
from rest_framework.response import Response

class TruckView(viewsets.ModelViewSet):  
    serializer_class = TruckSerializer   
    queryset = Truck.objects.all()   

class UserzView(viewsets.ModelViewSet):  
    serializer_class = UserzSerializer   
    queryset = Userz.objects.all()

class DriverView(viewsets.ModelViewSet):
    serializer_class = DriverSerializer
    queryset = Driver.objects.all()
