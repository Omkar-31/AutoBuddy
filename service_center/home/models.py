from django.db import models

# Create your models here.

class register(models.Model):

    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.BigIntegerField()
    password=models.CharField(max_length=255)
    user_type=models.CharField(max_length=255)

    class Meta:
        db_table="user_ecord"
