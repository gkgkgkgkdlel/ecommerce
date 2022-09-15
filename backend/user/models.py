from django.db import models
from product.models import Product


class User(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)


class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
