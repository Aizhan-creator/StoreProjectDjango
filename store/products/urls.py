from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'products'

urlpatterns = [
   path('', views.index, name='index'),
   path('products/', views.products, name='products'),
   path('users/', include('users.urls', namespace="users")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)