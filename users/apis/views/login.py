from rest_framework.generics import CreateAPIView
from ..serializers import LoginSerializer

class LoginView (CreateAPIView) : 
    serializer_class = LoginSerializer