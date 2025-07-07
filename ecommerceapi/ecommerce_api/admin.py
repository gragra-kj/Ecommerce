from django.contrib import admin

# Register your models here.
from .models import ProductModel,OrderItemModel,OrderModel,ShippingAddress

admin.site.register(ProductModel)
admin.site.register(OrderItemModel)
admin.site.register(OrderModel)
admin.site.register(ShippingAddress)