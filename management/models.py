from django.db import models
# Create your models here.
class Driver(models.Model):
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    driver_license = models.CharField(max_length=15)
    create_time = models.DateTimeField(auto_now_add=True)

