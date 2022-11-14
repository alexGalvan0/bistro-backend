from django.contrib.auth.models import User, Group
from .models import MenuItem, Category, Cuisine, Restaurant
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class CuisineSerializer (serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['title']


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['title']


class MenuItemSerializer(serializers.ModelSerializer):
    cuisine = CuisineSerializer()
    restaurant = RestaurantSerializer()
    category = CategorySerializer()

    class Meta:
        model = MenuItem
        fields = ['title', 'description', 'price',
                  'spicy_level', 'category', 'cuisine', 'restaurant']
