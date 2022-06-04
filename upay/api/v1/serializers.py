from rest_framework import serializers


class RegCardSerializer(serializers.Serializer):
    client_id = serializers.CharField(required=True)
    card_number = serializers.CharField(required=True)
    card_exp_date = serializers.CharField(required=True)
    card_holder_name = serializers.CharField(required=True)
    holder_phone_number = serializers.CharField(required=True)
    card_cvv = serializers.CharField(required=True)


