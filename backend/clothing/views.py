from django.shortcuts import render

from rest_framework import generics

from .serializers import ClothingSerializer
from .models import ClothingItem

class GetClothing(generics.ListAPIView):
    serializer_class = ClothingSerializer
    permission_classes = []
    queryset = ClothingItem.objects.all()

    # TODO: Will probably have to change this when we introduce searching


# TODO: Add/delete clothing?
# We might just use the admin page for doing this.
# Easier since we don't have to build a frontend...
class CreateClothingItem(generics.CreateAPIView):
    serializer_class = ClothingSerializer
    permission_classes = []
    queryset = ClothingItem.objects.all()
