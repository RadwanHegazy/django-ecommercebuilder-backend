from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from ..serializers import ProfileSerializer

class ProfileView (APIView) :
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get (self, request) :
        serializer = self.serializer_class(request.user)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        ) 