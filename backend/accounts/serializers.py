from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Bag, BagItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class BagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bag
        fields = ["id", "title", "description", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}


class BagItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BagItem
        fields = ["id", "bagParent", "clothingItem"]
        extra_kwargs = {"bagParent": {"read_only": True}}