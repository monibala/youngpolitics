from django.db import models

# Create your models here.
class blog_detail(models.Model):
    bname = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    bimage = models.ImageField(upload_to='image/blog/')
class contact (models.Model):
   
    name = models.CharField(max_length=100,default=True,blank=True)
    email = models.EmailField(max_length=100)
    number = models.IntegerField()
    service =  models.CharField(max_length=100, choices=(("DM",'Digital Marketing'),("Vc",'Voice Call'),("Sms",'Bulk Sms'),("Ivr",'IVR service'),("App",'Software/Mobile App')))
    comment = models.TextField(max_length=200,default=True,blank=True)