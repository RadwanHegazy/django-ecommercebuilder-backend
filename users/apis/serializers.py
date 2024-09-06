from rest_framework import serializers
from ..models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.validators import ValidationError

class LoginSerializer (serializers.Serializer) : 
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        try : 
            self.user = User.object.get(email=email)
        except User.DoesNotExist:
            raise ValidationError({
                'messsage' : 'invalid email'
            })
        
        if not self.user.check_password(password) : 
            raise ValidationError({
                'messsage' : 'invalid password'
            })
        
        return attrs

    def create(self, validated_data):
        return self.user  
    

    def to_representation(self, *args, **kwargs):
        tokens = RefreshToken.for_user(self.user)
        return {
            'access_token' : str(tokens.access_token),
            'refresh_token': str(tokens)
        }
    

class RegisterSerializer (serializers.ModelSerializer) : 
    class Meta:
        model = User
        fields = ['email','password', 'shop_name','phonenumber']

    def create(self, *args, **kwargs) : 
        self.user = User.object.create_user(**self.validated_data)
        self.user.save()
        return self.user
    
    def to_representation(self, *args, **kwargs):
        tokens = RefreshToken.for_user(self.user)
        return {
            'access_token' : str(tokens.access_token),
            'refresh_token': str(tokens)
        }
    


class ProfileSerializer (serializers.ModelSerializer) :
    class Meta:
        model = User
        fields = ['id','email','shop_name', 'phonenumber']