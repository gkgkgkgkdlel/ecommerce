# Generated by Django 4.1.1 on 2022-09-15 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("price", models.IntegerField(default=0)),
                ("description", models.TextField()),
                ("like_count", models.IntegerField(default=0)),
                (
                    "category_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.category",
                    ),
                ),
                (
                    "tag_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="product.tag"
                    ),
                ),
            ],
        ),
    ]
