from django.db import models
from management import models as mmodels

class Shipment(models.Model):
    truck_id = models.ForeignKey(mmodels.Truck, on_delete=models.CASCADE, null= True, blank=True)
    driver_id = models.ForeignKey(mmodels.Driver, on_delete=models.CASCADE, null= True, blank=True)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    loading_date = models.DateField()
    status = models.CharField(max_length=100, null= True, blank=True)
    shipper_id = models.ForeignKey(mmodels.Userz, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(f'{self.shipper_id} - {self.truck_id} - {self.driver_id}')
