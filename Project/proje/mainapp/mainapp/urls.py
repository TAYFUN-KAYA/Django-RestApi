
from django.contrib import admin
from django.urls import path,include
from .views import index,goster

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
    path('graph/',index),
    path('durum/',goster)
]
