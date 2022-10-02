from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from .serializers import UserSerializer
import json
import bcrypt
import re


@permission_classes((AllowAny,))
class LoginView(APIView):
    def post(self, request):
        print("들어옴 ")
        email = request.data.get("email")
        password = request.data.get("password")

        print(email)
        print(password)

        if email is None or password is None:
            return Response(
                {"error": "Please provide both username and password"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # 여기서 authenticate로 유저 validate
        # user = authenticate(email=email, password=password)
        user = authenticate(request, email=email, password=password)
        print(user)

        if not user:
            return Response(
                {"error": "Invalid credentials"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # user 로 토큰 발행
        token, _ = Token.objects.get_or_create(user=user)

        return Response({"token": token.key}, status=status.HTTP_200_OK)


@permission_classes((AllowAny,))
class TestView(APIView):
    def post(self, request):
        # data = json.loads(request.body)
        # password = data["password"]

        # print("password는 ", password)
        # hashed_password = bcrypt.hashpw(
        #     password.encode("utf-8"), bcrypt.gensalt()
        # )

        # decoded_password = hashed_password.decode("utf-8")
        # data["password"] = decoded_password

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({"Test중입니다."})
