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

from product.models import Product

from .serializers import OrderSerializer, OrderDetailSerializer
from user.models import User
from .models import Order, OrderDetails
from product.serializers import ProductSerializer


@permission_classes((AllowAny,))
class ReadOrderView(APIView):
    def get(self, request, order_id):
        """
        사용자가 주문한 주문서를 반환함.
        """

        order = Order.objects.get(id=order_id)
        order_serializer = OrderSerializer(order)

        print("order_serializer.data는 ", order_serializer.data)

        result = {"order": order_serializer.data}

        return Response({"result": result}, status=status.HTTP_200_OK)


@permission_classes((AllowAny,))
class CreateOrderView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        user = User.objects.get(email=request.user)
        data["user_id"] = user.id

        serializer = OrderSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            order_id = Order.objects.latest("id").id
            order_detail = {}
            order_detail["order_id"] = order_id

            product_list = data["products"]

            for product in product_list:

                order_detail["product_id"] = product["id"]
                order_detail["product_quantity"] = product["quantity"]
                aaa = order_detail["product_id"]

                product_price = Product.objects.get(id=aaa).price

                order_detail["product_total_price"] = (
                    order_detail["product_quantity"] * product_price
                )

                serializer = OrderDetailSerializer(data=order_detail)

                if serializer.is_valid():
                    serializer.save()

                else:
                    return Response(
                        {"message": "FAILED"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

            return Response(
                {"message": "SUCCESS"}, status=status.HTTP_201_CREATED
            )

        else:
            return Response(
                {"message": "FAILED"}, status=status.HTTP_400_BAD_REQUEST
            )
