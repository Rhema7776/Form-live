from django.db import models

# Create your models here.
class User(models.Model):
    First_name = models.CharField(max_length=30, default = "")
    Last_name = models.CharField(max_length=40,default = "")
    des= models.TextField(max_length=200,default = "")
    phone = models.CharField( max_length = 11, default= "")

    def __str__(self):
        return self.First_name
    