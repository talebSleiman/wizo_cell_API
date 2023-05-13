from django.contrib import admin
from .models import Product
# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ('name','price','type','category')

admin.site.register(Product, AdminProduct)