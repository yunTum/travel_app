from django.contrib.auth.models import User

from .models import Plan
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
