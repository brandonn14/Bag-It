from rest_framework import serializers

from .models import ClothingItem

class ClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothingItem
        fields = [
            "name",
            "description",
            "price",
            "size",
            "type",
            "gender",
            "brand",
            "image",
        ]