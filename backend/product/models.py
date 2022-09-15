from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField()
    like_count = models.IntegerField(default=0)
    category_id = models.ForeignKey(
        "product.Category", on_delete=models.CASCADE
    )
    tag_id = models.ForeignKey("product.Tag", on_delete=models.CASCADE)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
