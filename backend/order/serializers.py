from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "user_id",
            "address",
            "receiver_name",
            "total_price",
            "delivery_fee",
        ]
