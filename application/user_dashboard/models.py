from django.db import models
# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email_address = models.EmailField(null=False, unique=False)
    # password_user = models.CharField(max_length=20, null=False)
    vehicle_sign = models.CharField(max_length=50, null=False, unique=True)

class Vehicle_detail(models.Model):
    model_no = models.CharField(max_length=20, unique=True, null=False, default='ACS')
    chasis_no = models.CharField(max_length=20, unique=True, null=False, default='DEFAULT-CHASIS-NO')
    vehicle_type = models.CharField(max_length=20, null=False, default='CAMPUS-SHUTTLE')
    vehicle_sign = models.CharField(max_length=50, unique=True, null=False, default='DEFAULT-VEHICLE-SIGNATURE')
    mfg_date = models.DateField(null=False, auto_now_add=True)

    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='vehicles', null=True)
    