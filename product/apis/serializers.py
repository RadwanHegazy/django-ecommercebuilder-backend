from ..models import Product
from rest_framework import serializers

class PdSerializer (serializers.ModelSerializer) : 
    class Meta:
        model = Product
        exclude = ['user']

    def validate(self, attrs):
        attrs['user'] = self.context.get('user')
        return attrs