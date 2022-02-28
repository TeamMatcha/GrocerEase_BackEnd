from rest_framework import serializers
from .models import User, List, Tag, ListItem


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("tag",)


class Categories(object):
    def __init__(self, choices):
        self.choices = choices


CATEGORIES = (
    ("Produce"),
    ("Dairy"),
    ("Baked Goods"),
    ("Meat and Fish"),
    ("Snacks"),
    ("Alcohol"),
    ("Baby Care"),
    ("Canned Goods"),
    ("Dry Goods"),
    ("Sauces and  Condiments"),
    ("Herbs and Spices"),
    ("Non-Alcoholic Beverages"),
    ("Household and Cleaning"),
    ("Health and Beauty"),
    ("Pet Care"),
    ("Frozen Goods"),
)


class ItemSerializer(serializers.ModelSerializer):
    choices = serializers.ChoiceField(choices=CATEGORIES)

    class Meta:
        model = ListItem
        fields = (
            "pk",
            "list",
            "name",
            "item_quantity",
            "choices",
        )
        read_only_fields = ["list", "choices"]


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ("pk", "name", "user", "tags", "date_created")
        read_only_fields = ["user"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")
