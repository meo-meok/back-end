from rest_framework import serializers
# from django.contrib.auth.models import User
from .models import Restaurant, Users, Review

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'