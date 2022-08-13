from rest_framework import serializers
from .models import Truck

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ('id' ,'plate_number', 'plate_type', 'truck_type', 'production_year', 'status')