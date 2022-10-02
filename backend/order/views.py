from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
import json
import bcrypt
import re
from rest_framework.pagination import PageNumberPagination

from .serializers import OrderSerializer
from user.models import User

# Create your views here.
@permission_classes((AllowAny,))
class CreateOrderView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        user = User.objects.get(email=request.user)
        data["user_id"] = user.id

        serializer = OrderSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "SUCCESS"}, status=status.HTTP_201_CREATED
            )

        return Response(
            {"message": "FAILED"}, status=status.HTTP_400_BAD_REQUEST
        )
