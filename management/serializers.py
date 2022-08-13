from rest_framework import serializers
from .models import Truck, Userz

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ('id' ,'plate_number', 'plate_type', 'truck_type', 'production_year', 'status')

class UserzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userz
        fields = ('id' ,'name', 'role')
