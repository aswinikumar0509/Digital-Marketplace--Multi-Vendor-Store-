# Generated by Django 4.2.15 on 2024-08-22 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0002_product_seller_orderdetail"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="total_sales",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="product",
            name="total_sales_amount",
            field=models.IntegerField(default=0),
        ),
    ]
