# Generated by Django 4.2.5 on 2023-11-11 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0005_service_record_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_record',
            name='appintment_date',
            field=models.CharField(max_length=500),
        ),
    ]
