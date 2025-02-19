from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        read_only_fields = (
            'created_at',
            'created_by',
            'modified_at'
        ),
        fields = (
            "id",
            "item", 
            "car_name",
            "car_model",
            "car_engine",
            "car_vin",
            "item_number",
            "status",
        )