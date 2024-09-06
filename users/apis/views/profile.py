from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from ..serializers import ProfileSerializer
from product.models import Product

class ProfileView (APIView) :
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get (self, request) :
        user = request.user
        serializer = self.serializer_class(user)
        products = Product.objects.filter(user=user)
        data = {
            'products' : products.values('title','price'),
            'count' : products.count(),
            **serializer.data
        }
        return Response(
            data,
            status=status.HTTP_200_OK
        ) 