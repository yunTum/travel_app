from django.contrib.auth.models import User

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

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('place', 'price' , 'chara', 'photo', 'explain')

class CardToCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CardToCard
        fields = ('fromcard', 'tocard' , 'duration', 'price')

class PlaceNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceName
        fields = ('name')