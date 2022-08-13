from django.contrib import admin
from .models import Driver, Truck, Userz

admin.site.register(Truck)
admin.site.register(Userz)
admin.site.register(Driver)