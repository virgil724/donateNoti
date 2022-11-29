from rest_framework import serializers
from .models import Streamer, Opay, Ecpay


class StreamerSerializer(serializers.ModelSerializer):
    deleteKey = serializers.ReadOnlyField()

    class Meta:
        model = Streamer
        fields = ["twitchId", "opayId", "ecpayId", "deleteKey"]
