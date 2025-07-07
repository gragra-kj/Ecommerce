from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,OrderItemViewSet,OrderViewSet,ShippinngAddressViewsets
from django.urls import path,include




router=DefaultRouter()

router.register('products',ProductViewSet)
router.register('order',OrderViewSet)
router.register('order-item',OrderItemViewSet)
router.register('shipping-address',ShippinngAddressViewsets)

urlpatterns=[
    path('',include(router.urls))
]

