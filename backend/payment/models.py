from django.db import models

# Create your models here.
from order.models import Order


class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    method = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
