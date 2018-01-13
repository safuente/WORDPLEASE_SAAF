from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView

from rest_framework.response import Response


class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    password = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()

    def get_username(self, instance):
       username = instance.username
       return username

    def validate_username(self,data):
        if self.instance is None and User.objects.filter(username=data).exists():
            raise ValidationError("Username already exists")
        if self.instance is not None and self.instance.username != data and User.objects.filter(username=data).exists():
            raise ValidationError("Required username is already in use")
        return data


    def create(self, validated_data):
        instance = User()
        instance.username = validated_data.get("username")
        instance.set_password(validated_data.get("password"))
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.email = validated_data.get("email")
        instance.save()
        return instance

    def update(self, instance, validated_data):
        instance.username = validated_data.get("username")
        instance.set_password(validated_data.get("password"))
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.email = validated_data.get("email")
        instance.save()
        return instance




