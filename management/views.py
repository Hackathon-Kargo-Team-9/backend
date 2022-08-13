from django.shortcuts import render
from .serializers import TruckSerializer, UserSerializer
from rest_framework import viewsets      
from .models import Truck, User               

class TruckView(viewsets.ModelViewSet):  
    serializer_class = TruckSerializer   
    queryset = Truck.objects.all()   

class UserView(viewsets.ModelViewSet):  
    serializer_class = UserSerializer   
    queryset = User.objects.all()   