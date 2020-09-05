from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Plan, Card, CardToCard, PlaceName
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ A serializer class for the User model """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username',
                  'password', 'is_active', 'is_superuser')


class PlanSerializer(serializers.ModelSerializer):
    """ A serializer for the Plan model """
    class Meta:
        model = Plan
        fields = ('id', 'name', 'description', 'status')

class PlaceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceName
        fields = "__all__"

class CardSerializer(serializers.ModelSerializer):
    place  = PlaceNameSerializer()
    class Meta:
        model = Card
        fields = ('id', 'place', 'price' , 'chara', 'photo', 'explain')

class CardToCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardToCard
        fields = ('id', 'fromcard', 'tocard' , 'duration', 'price')
