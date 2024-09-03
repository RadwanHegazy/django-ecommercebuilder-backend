from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class BaseUserObjects (BaseUserManager) : 
    def create_user(self, password, **fields) :
        user = self.model(**fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,**fields) :
        fields['is_staff'] = True
        fields['is_superuser'] = True
        return self.create_user(**fields)


class User (AbstractUser) : 
    object = BaseUserObjects()

    first_name = None
    last_name = None
    username = None

    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=20, unique=True, null=True, blank=True)
    shop_name = models.SlugField(max_length=225, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['shop_name','phonenumber']

    def __str__(self) -> str:
        return self.shop_name

