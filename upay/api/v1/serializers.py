from rest_framework import serializers


class RegCardSerializer(serializers.Serializer):
    card_number = serializers.CharField(required=True)
    card_exp_date = serializers.CharField(required=True)
    card_holder_name = serializers.CharField(required=True)
    holder_phone_number = serializers.CharField(required=True)
    card_cvv = serializers.CharField(required=True)


class CreateHoldSerializer(serializers.Serializer):
    card_token = serializers.CharField(required=True)
    amount = serializers.IntegerField(required=True)


class PayHoldSerializer(serializers.Serializer):
    amount = serializers.IntegerField(required=True)
    hold_id = serializers.IntegerField(required=True)


class CheckHoldSerializer(serializers.Serializer):
    _type = serializers.CharField(required=True)
    target = serializers.CharField(required=True)


class CancelHoldSerializer(serializers.Serializer):
    hold_id = serializers.IntegerField(required=True)
