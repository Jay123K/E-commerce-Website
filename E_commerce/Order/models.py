from django.db import models
from app1.models import Customer
from Category.models import Product
import datetime
# Create your models here.


class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField(default=1)
    price=models.PositiveSmallIntegerField
    date=models.DateField(default=datetime.datetime.today)