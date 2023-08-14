from rest_framework import serializers
from shorter import models

# from small_auth.simple_sign import create_sing
# from django.conf import settings


class AddressSerializer(serializers.Serializer):
    id = serializers.UUIDField(required=False)
    url = serializers.URLField(required=True, max_length=models.MAX_URL_LENTH)

    def create(self, validated_data):
        # TODO: fix for http:// and https://
        # url = validated_data['url'].split('http://')[-1]
        # validated_data['url'] = url

        return models.Address.objects.create(**validated_data)