from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField()
    like_count = models.IntegerField(default=0)
    category_id = models.ForeignKey(
        "product.Category", on_delete=models.CASCADE, null=True
    )
    tag_id = models.ForeignKey(
        "product.Tag", on_delete=models.CASCADE, null=True
    )


class ProductImag(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.ImageField(upload_to="appname", null=True)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
