# Generated by Django 4.2.5 on 2023-11-06 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_order_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='service_obj',
        ),
    ]
