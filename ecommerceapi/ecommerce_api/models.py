from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductModel(models.Model):
    name=models.CharField(max_length=120)
    description=models.TextField(max_length=200)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock_quantity=models.PositiveIntegerField()
    date_created=models.DateTimeField(auto_now_add=True)
    
class OrderModel(models.Model):
    customer=models.ForeignKey(User, on_delete=models.CASCADE)    
    date_created=models.DateTimeField(auto_now_add=True)
    completed=models.BooleanField(default=False)
    
class OrderItemModel(models.Model):
    order=models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name="items")
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    
class ShippingAddress(models.Model):
    address=models.CharField(max_length=200)
    zipcode=models.CharField(max_length=10)
    country=models.CharField(max_length=120)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    order=models.ForeignKey(OrderModel,on_delete=models.CASCADE)