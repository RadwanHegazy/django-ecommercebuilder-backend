from django.contrib import admin
from .models import User


@admin.register(User)
class UserPanel (admin.ModelAdmin) : 
    list_display = ['email', 'shop_name']