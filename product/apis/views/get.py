from rest_framework.views import APIView
from ..serializers import PdSerializer, Product
from users.models import User
from rest_framework import status
from rest_framework.response import Response

class GetProductList (APIView) : 
    serialier_class = PdSerializer

    def get (self, request, shop_name) :
        try : 
            user_shop = User.object.get(shop_name=shop_name)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        query = Product.objects.filter(user=user_shop)
        serializer = self.serialier_class(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    