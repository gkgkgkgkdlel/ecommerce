from rest_framework import serializers
from .models import Order, OrderDetails


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


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = [
            "order_id",
            "product_id",
            "product_quantity",
            "product_total_price",
        ]
