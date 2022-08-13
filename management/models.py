from django.db import models

class Truck(models.Model):
    plate_number = models.CharField(max_length=100)
    plate_type = models.CharField(max_length=100)
    truck_type = models.CharField(max_length=100)
    production_year = models.IntegerField()
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.plate_number

class Userz(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name