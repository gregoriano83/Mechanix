from django.contrib import admin

from .models import Order



class OrderAdmin(admin.ModelAdmin):
    list_filter = [
        'created_by',
        'car_model',
        'item',
        'created_at'

    ]
    list_display = ("created_by", "item","car_name", "car_model", "created_at")


    

admin.site.register(Order, OrderAdmin)