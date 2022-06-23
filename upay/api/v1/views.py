from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RegCardSerializer
from .serializers import PayHoldSerializer
from .serializers import CheckHoldSerializer
from .serializers import CancelHoldSerializer
from .serializers import CreateHoldSerializer

from upay.libupay.uclient import upay_client


class RegCardView(APIView):
    """1 Method partnerRegisterCardIPS
       The method requests permission to register the card in the payment system.
    """
    def post(self, request):
        serializer = RegCardSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        resp = upay_client.reg_card(**serializer.validated_data)
        
        return Response(resp, status=status.HTTP_200_OK)


class CreateHoldView(APIView):
    """2 Method partnerHoldCreateIPS
      The method requests to create a new hold in the payment system.
    """
    def post(self, request):
        serializer = CreateHoldSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        resp = upay_client.hold_create(**serializer.validated_data)
        
        return Response(resp, status=status.HTTP_200_OK)


class PayHoldView(APIView):
    """3 Method partnerHoldCreateIPS
        The method requests to pay hold in the payment system
    """
    def post(self, request):
        serializer = PayHoldSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        resp = upay_client.pay_hold(**serializer.validated_data)
        
        return Response(resp, status=status.HTTP_200_OK)


class CheckHoldView(APIView):
    """4 Method partnerHoldCheckIPS
        The method requests to check hold status in the payment system
    """
    def post(self, request):
        serializer = CheckHoldSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        resp = upay_client.check_hold(**serializer.validated_data)
        
        return Response(resp, status=status.HTTP_200_OK)


class CancelHoldView(APIView):
    """5 Method partnerHoldRequestIPS
        The method requests to cancel hold in the payment system
    """
    def post(self, request):
        serializer = CancelHoldSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        resp = upay_client.cancel_hold(**serializer.validated_data)
        
        return Response(resp, status=status.HTTP_200_OK)