# registration/models.py

from django.db import models

class Customer(models.Model):
    customer_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    aadhaar = models.CharField(max_length=12, unique=True)
    pincode = models.CharField(max_length=6)

class SavingsAccount(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    initial_amount = models.DecimalField(max_digits=10, decimal_places=2)
