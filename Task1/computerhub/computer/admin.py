from django.contrib import admin

# Register your models here.
from .models import Computer, ComputerBrands, ComputerSpecification

admin.site.register(Computer)
admin.site.register(ComputerBrands)
admin.site.register(ComputerSpecification)