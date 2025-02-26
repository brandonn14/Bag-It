from django.urls import path

from . import views

urlpatterns = [
    path("", views.GetClothing.as_view(), name="get_clothing"),
    path("create/", views.CreateClothingItem.as_view(), name="create_clothing"),
    
]