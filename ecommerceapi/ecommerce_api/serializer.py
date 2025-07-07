from rest_framework import serializers

from .models import ProductModel,OrderItemModel,OrderModel,ShippingAddress


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields='__all__'
  
class OrderitemSerializer(serializers.ModelSerializer):
    product = serializers.HyperlinkedRelatedField(
        view_name='productmodel-detail',
        read_only=True,
        lookup_field='pk'  # or 'slug' if you're using slugs
    )

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
        fields=['id','customer','status','date_created','items','total_price']
                                