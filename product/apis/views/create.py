from rest_framework.views import APIView
from ..serializers import PdSerializer
from rest_framework import status, permissions
from rest_framework.response import Response

class CreateProducts (APIView) : 
    serialier_class = PdSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request) : 
        serializer = self.serialier_class(request.data, context={'user':request.user})
        if serializer.is_valid() : 
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
