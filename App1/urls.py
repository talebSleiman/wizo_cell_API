
from django.urls import path, include
from .views import products


urlpatterns = [
    path('products/', products),
]
