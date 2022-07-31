from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ('CAR INFORMATION', {'fields': ['brand']}),
        ('TIME INFORMATION', {'fields': ['year']}),
    ]


admin.site.register(Car, CarAdmin)
