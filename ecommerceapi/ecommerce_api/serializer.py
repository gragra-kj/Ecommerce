from rest_framework import serializers

from .models import ProductModel,OrderItemModel,OrderModel,ShippingAddress

class ProductSummarySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='productmodel-detail',
        lookup_field='pk'
    )

    class Meta:
        model = ProductModel
        fields = ['id', 'name', 'url']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields='__all__'
  

class OrderitemSerializer(serializers.ModelSerializer):
    product = ProductSummarySerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=ProductModel.objects.all(),
        write_only=True,
        source='product'
    )

    order_id = serializers.PrimaryKeyRelatedField(
        queryset=OrderModel.objects.all(),
        write_only=True,
        source='order'
    )

    class Meta:
        model = OrderItemModel
        fields = ['id', 'order', 'order_id', 'product', 'product_id', 'quantity']        
class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=ShippingAddress
        fields='__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    items=OrderitemSerializer(many=True,read_only=True)
    class Meta:
        model=OrderModel
        fields=['id','customer','status','date_created','items','total_price']
                                