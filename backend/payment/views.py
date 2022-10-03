from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
import json
from .models import Payment
from user.models import User
from order.models import Order
from .serializers import PaymentSerializer


@permission_classes((IsAuthenticated,))
class ReadPaymentView(APIView):
    """
    payment_id에 해당하는 결제 내역을 반환함.
    """

    def get(self, request, payment_id):
        payment_obj = Payment.objects.get(id=payment_id)
        pay_serializer = PaymentSerializer(payment_obj)

        print("pay_serializer.data는 ", pay_serializer.data)

        result = {"payment": pay_serializer.data}

        return Response({"result": result}, status=status.HTTP_200_OK)


@permission_classes((IsAuthenticated,))
class CreatePaymentView(APIView):
    """
    order_id에 해당하는 주문 내역을 결제함.
    """

    def post(self, request):
        data = json.loads(request.body)
        order_id = data["order_id"]
        order_obj = Order.objects.get(id=order_id)
        data["amount"] = order_obj.total_price

        serializer = PaymentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"message": "SUCCESS"}, status=status.HTTP_201_CREATED
            )

        else:
            print(serializer.errors)

            return Response(
                {"message": "FAILED"}, status=status.HTTP_400_BAD_REQUEST
            )


@permission_classes((IsAuthenticated,))
class DeletePaymentView(APIView):
    """
    결제를 취소하는 api
    """

    def delete(self, request, payment_id):
        payment_obj = Payment.objects.get(id=payment_id)
        payment_obj.delete()

        return Response({"message": "SUCCESS"}, status=status.HTTP_200_OK)
