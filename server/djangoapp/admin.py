from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class

admin.site.register(CarMake)
admin.site.register(CarModel)

# Register models here
