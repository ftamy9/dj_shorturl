from rest_framework import serializers
from small_auth.models import BaseUser
from small_auth.simple_sign import create_sing

from django.conf import settings


class UserSerializer(serializers.Serializer):
    id = serializers.CharField(required=True, max_length=10)
    password_hash = serializers.CharField(required=True, max_length=32)

    def create(self, validated_data):

        raw_password = validated_data['password_hash']
        validated_data['password_hash'] = create_sing(raw_password.encode(), settings.PASSWORD_SECRET)
        user = BaseUser.objects.create(**validated_data)
        # Just mask the hash!
        user.password_hash='ok***hash'

        return user
