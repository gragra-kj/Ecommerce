from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ecommerce_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/ecommerce/', include('ecommerce_api.routers')),
    path('', views.ecommerce_frontend_view, name='frontend'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    #path('auth/', include('rest_framework_social_oauth2.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
