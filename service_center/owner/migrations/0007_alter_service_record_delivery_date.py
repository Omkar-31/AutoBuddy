# Generated by Django 4.2.5 on 2023-11-11 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0006_alter_service_record_appintment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service_record',
            name='delivery_date',
            field=models.CharField(blank=True, default='Not Deliverd', max_length=255, null=True),
        ),
    ]
