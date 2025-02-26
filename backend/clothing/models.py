from django.db import models
from enum import Enum

# -- Clothing enums --
class Size(models.IntegerChoices):
    EXTRA_SMALL = 0
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    EXTRA_LARGE = 4

class Type(models.IntegerChoices):
    SHORTS = 0
    PANTS = 1
    T_SHIRT = 2
    DRESS = 3
    SHOES = 4
    HAT = 5

class Gender(models.IntegerChoices):
    MALE = 0
    FEMALE = 1
    UNISEX = 2

class Brand(models.TextChoices):
    NIKE = "Nike"
    JORDAN = "Jordan"
    TOMMY_HILFIGER = "Tommy Hilfiger"
    GUCCI = "Gucci"


class ClothingManager(models.Manager):
    def create(self, 
               name: str, 
               description: str,
               price: float,
               size: Size,
               type: Type,
               gender: Gender,
               brand: Brand
        ):
        # Validate fields (this is horrible)
        if not name:
            raise ValueError("ClothingItems require a name")
        if not description:
            raise ValueError("ClothingItems require a description")
        if not price:
            raise ValueError("ClothingItems require a price")
        if not size:
            raise ValueError("ClothingItems require a size")
        if not type:
            raise ValueError("ClothingItems require a type")
        if not gender:
            raise ValueError("ClothingItems require a gender")
        if not brand:
            raise ValueError("ClothingItems require a brand")
        
        item = self.model(
            name = name,
            description = description,
            price = price,
            size = size,
            type = type,
            gender = gender,
            brand = brand
        )
        item.save()
        return item


class ClothingItem(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    size = models.IntegerField(choices=Size)
    type = models.IntegerField(choices=Type)
    gender = models.IntegerField(choices=Gender)
    brand = models.TextField(choices=Brand)
    image = models.ImageField(default='fallback.png', blank=True)

    # Set manager
    objects = ClothingManager()

    def __str__(self):
        return self.name

