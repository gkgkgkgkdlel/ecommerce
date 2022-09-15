from django.db import models

# Create your models here.
from user.models import User
from product.models import Product


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    receiver_name = models.CharField(max_length=100)
    order_status = models.CharField(max_length=100)
    payment_status = models.BooleanField(default=False)
    total_product_price = models.IntegerField(default=0)
    delivery_fee = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    method = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    amout = models.IntegerField(default=0)
    depositor_name = models.CharField(max_length=100)
    deposit_bank = models.CharField(max_length=100)
