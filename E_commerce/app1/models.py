from django.db import models

# Create your models here.

class Customer(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    email=models.EmailField(null=False,blank=False)
    password=models.CharField(null=False,blank=False)
    address=models.TextField(null=False,blank=False)
    age=models.PositiveSmallIntegerField(null=False,blank=False)
    contact=models.CharField(max_length=10,null=False,blank=False)

    def __str__(self):
        return self.name



