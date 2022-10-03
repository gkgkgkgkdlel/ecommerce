from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "order_id",
            "method",
            "amount",
            "date",
            "status",
        ]
