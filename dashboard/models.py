from distutils.command.upload import upload
from django.db import models

# Create your models here.
class voterlist(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=50, choices=(("M",'Male'),("F",'Female')))
    address = models.TextField(max_length=500)
    images = models.ImageField(upload_to='image/voter/',blank=True,null=True)

class elec_res(models.Model):
    year = models.IntegerField(null=True,blank=True)
    party = models.CharField(max_length=100)
    seats = models.IntegerField()
    vote = models.DecimalField(max_digits=4,decimal_places=2,null=True,blank=True)

class my_team (models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    images = models.ImageField(upload_to='image/team/',blank=True,null=True)