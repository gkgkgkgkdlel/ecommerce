from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.decorators import permission_classes
import json
import bcrypt
import re
from rest_framework.pagination import PageNumberPagination
from .pagination import PaginationHandlerMixin
from .serializers import CategorySerializer, ProductSerializer, TagSerializer
from .models import Product


class ProductPagination(PageNumberPagination):
    page_size = 10


@permission_classes((IsAdminUser,))
class CreateProductView(APIView):
    def post(self, request):
        """
        제품을 생성하는 api.
        """

        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "SUCCESS"}, status=status.HTTP_201_CREATED
            )

        return Response(
            {"message": "FAILED"}, status=status.HTTP_400_BAD_REQUEST
        )


@permission_classes((AllowAny,))
class ReadProductView(APIView, PaginationHandlerMixin):
    pagination_class = ProductPagination
    serializer_class = ProductSerializer

    def get(self, request):
        """
        한 페이지당 10개의 제품을 제품명 오름차순으로 리스트를 반환함.
        """

        product_list = Product.objects.order_by("name")
        page = self.paginate_queryset(product_list)

        if page is not None:
            serializer = self.get_paginated_response(
                self.serializer_class(page, many=True).data
            )
        else:
            serializer = self.serializer_class(product_list, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


@permission_classes((IsAdminUser,))
class UpdateProductView(APIView):
    serializer_class = ProductSerializer

    def put(self, request):
        """
        제품 정보를 수정하는 api.
        """

        data = json.loads(request.body)
        product_id = data["product_id"]
        product_obj = Product.objects.get(id=product_id)

        serializer = self.serializer_class(product_obj, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "SUCCESS"}, status=status.HTTP_201_CREATED
            )
        else:
            print("serializer.errors는 ", serializer.errors)

        return Response(
            {"message": "FAILED"}, status=status.HTTP_400_BAD_REQUEST
        )


@permission_classes((IsAdminUser,))
class DeleteProductView(APIView):
    def delete(self, request, product_id):
        """
        제품을 삭제하는 api.
        """

        product_obj = Product.objects.get(id=product_id)
        product_obj.delete()

        return Response({"message": "SUCCESS"}, status=status.HTTP_200_OK)


@permission_classes((IsAdminUser,))
class CreateCategoryView(APIView):
    def post(self, request):
        """
        제품 카테고리를 생성하는 api.
        """
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "SUCCESS"}, status=status.HTTP_201_CREATED
            )

        return Response(
            {"message": "FAILED"}, status=status.HTTP_400_BAD_REQUEST
        )


@permission_classes((IsAdminUser,))
class CreateTagView(APIView):
    def post(self, request):
        """
        제품 태그를 생성하는 api.
        """
        serializer = TagSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "SUCCESS"}, status=status.HTTP_201_CREATED
            )

        return Response(
            {"message": "FAILED"}, status=status.HTTP_400_BAD_REQUEST
        )
