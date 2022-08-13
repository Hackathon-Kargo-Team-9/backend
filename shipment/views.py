from django.shortcuts import render
from .serializers import ShipmentSerializer
from rest_framework import viewsets      
from .models import Shipment              

class ShipmentView(viewsets.ModelViewSet):  
    serializer_class = ShipmentSerializer   
    queryset = Shipment.objects.all()   
