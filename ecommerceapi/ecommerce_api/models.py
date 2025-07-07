from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class ProductModel(models.Model):
    name=models.CharField(max_length=120)
    description=models.TextField()
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock_quantity=models.PositiveIntegerField()
    date_created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    
class OrderModel(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('SHIPPED', 'Shipped'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    date_created= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.pk} by {self.customer.username}"
    
class OrderItemModel(models.Model):
    order=models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name="items")
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
class ShippingAddress(models.Model):
    address=models.CharField(max_length=200)
    zipcode=models.CharField(max_length=10)
    country=models.CharField(max_length=120)
    customer=models.ForeignKey(User,on_delete=models.CASCADE)
    order=models.ForeignKey(OrderModel,on_delete=models.CASCADE)