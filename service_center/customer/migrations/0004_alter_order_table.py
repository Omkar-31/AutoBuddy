# Generated by Django 4.2.5 on 2023-11-06 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_alter_order_service_obj'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='order',
            table='appointment',
        ),
    ]
