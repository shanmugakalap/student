from django.db import models

class studentmodel(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    dept = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=15)
    DOB = models.DateField(null=True, blank=True)

def __str__(self):
    return self.name
# Create your models here.
