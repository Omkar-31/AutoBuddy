# Generated by Django 4.2.5 on 2023-11-11 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0002_service_record_service_record_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_record',
            name='delivery_date',
            field=models.DateField(default='0000-00-00', null=True),
        ),
        migrations.AlterField(
            model_name='service_record_detail',
            name='delivery_date',
            field=models.DateField(default='0000-00-00', null=True),
        ),
    ]
