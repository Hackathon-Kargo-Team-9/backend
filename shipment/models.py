from django.db import models
from management import models as mmodels

class Shipment(models.Model):
    license_number = models.ForeignKey(mmodels.Truck, on_delete=models.CASCADE)
    #driver_name = models.ForeignKey(mmodels.Driver, on_delete=models.CASCADE)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    loading_date = models.DateField()
    status = models.CharField(max_length=100)
    shipper_id = models.ForeignKey(mmodels.Userz, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(f'{self.shipper_id} - {self.license_number}')
