# Generated by Django 3.1.5 on 2021-01-26 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20210126_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='orders',
            field=models.ManyToManyField(related_name='related_customer', to='mainapp.Order', verbose_name='Заказы покупателя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='cust',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_orders', to='mainapp.customer', verbose_name='Покупатель'),
        ),
    ]
