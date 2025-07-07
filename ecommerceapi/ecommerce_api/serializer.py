from rest_framework import serializers

from .models import ProductModel,OrderItemModel,OrderModel,ShippingAddress


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields='__all__'
  
class OrderitemSerializer(serializers.ModelSerializer):
    class Meta:
        model=OrderItemModel
        fields='__all__'

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShippingAddress
        fields='__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    items=OrderitemSerializer(many=True,read_only=True)
    class Meta:
        model=OrderModel
        fields=['id','customer','completed','created_on','items']
                                