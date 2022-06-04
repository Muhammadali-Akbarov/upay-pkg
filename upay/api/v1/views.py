from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RegCardSerializer

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


class HoldCreateView(APIView):
    """Coming soon!"""
    def post(self, request):
        pass


class HoldPayView(APIView):
    """Coming soon!"""
    def post(self, request):
        pass


class HoldCheck(APIView):
    """Coming soon!"""
    def post(self, request):
        pass