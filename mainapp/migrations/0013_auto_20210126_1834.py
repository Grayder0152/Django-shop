# Generated by Django 3.1.5 on 2021-01-26 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_order_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_customer', to='mainapp.Order', verbose_name='Заказы покупателя'),
        ),
    ]
