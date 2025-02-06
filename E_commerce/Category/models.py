from django.db import models

# Create your models here.

class Category(models.Model): 
    name = models.CharField(max_length=50) 

  
    def __str__(self): 
        return self.name 
    

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    p_name=models.CharField(max_length=50)
    price=models.PositiveSmallIntegerField(default=0)
    image=models.ImageField(upload_to='upload/product/')
