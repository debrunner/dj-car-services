# Generated by Django 4.2.7 on 2023-11-11 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_order_options_rename_vehicles_order_vehicle_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
    ]
