from ..models import Product
from rest_framework import serializers

class PdSerializer (serializers.ModelSerializer) : 
    class Meta:
        model = Product
        exclude = ['user']

    def validate(self, attrs):
        attrs['user'] = self.context.get('user')
        return attrs
    
    def to_representation(self, instance:Product):
        data = super().to_representation(instance)
        data['phonenumber'] = instance.user.phonenumber
        return data