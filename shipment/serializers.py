from rest_framework import serializers
from .models import Shipment

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ('id' ,'license_number', 'origin', 'destination', 'loading_date', 'status', 'shipper_id')
