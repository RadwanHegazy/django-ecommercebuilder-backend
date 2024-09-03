from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductPanel (admin.ModelAdmin): 
    list_display = ['title','user','price']
