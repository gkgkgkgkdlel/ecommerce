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
from .serializers import CategorySerializer, ProductSerializer, TagSerializer


@permission_classes((AllowAny,))
class CreateProductView(APIView):
    def post(self, request):

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "SUCCESS"}, status=status.HTTP_201_CREATED
            )

        return Response({"테스트 중입니다."})


@permission_classes((AllowAny,))
class CreateCategoryView(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "SUCCESS"}, status=status.HTTP_201_CREATED
            )

        return Response({"테스트 중입니다."})


@permission_classes((AllowAny,))
class CreateTagView(APIView):
    def post(self, request):

        serializer = TagSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "SUCCESS"}, status=status.HTTP_201_CREATED
            )

        return Response({"테스트 중입니다."})
