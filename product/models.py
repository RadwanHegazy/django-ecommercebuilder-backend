from django.db import models
from users.models import User


class Product (models.Model) : 
    image = models.ImageField(upload_to='pd-pics/')
    title = models.CharField(max_length=225)
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_pd')


    def __str__(self) -> str:
        return self.title
