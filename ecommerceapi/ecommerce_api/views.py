from django.shortcuts import render
from .models import OrderItemModel,OrderModel,ProductModel,ShippingAddress
from .serializer import OrderitemSerializer,OrderSerializer,ProductSerializer,ShippingAddressSerializer
from rest_framework import viewsets,permissions

def ecommerce_frontend_view(request):
    return render(request, 'ecommerce_api/frontend.html')

class OrderViewSet(viewsets.ModelViewSet):
    queryset=OrderModel.objects.all()
    serializer_class=OrderSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

    
    
class ProductViewSet(viewsets.ModelViewSet):
    queryset=ProductModel.objects.all()
    serializer_class=ProductSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
        
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset=OrderItemModel.objects.all()
    serializer_class=OrderitemSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]
    
class ShippinngAddressViewsets(viewsets.ModelViewSet):
    queryset=ShippingAddress.objects.all()
    serializer_class=ShippingAddressSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]    

# Create your views here.
