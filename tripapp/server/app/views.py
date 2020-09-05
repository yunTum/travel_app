from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import generics, permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser

from .models import Plan, Card, CardToCard, PlaceName
from .serializers import UserSerializer, PlanSerializer, CardSerializer, CardToCardSerializer, PlaceNameSerializer


class UserList(generics.ListAPIView):
    """ View to list all users"""
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    #permission_classes = (permissions.IsAuthenticated,)


class UserCreate(generics.CreateAPIView):
    """ View to create a new user. Only accepts POST requests """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (permissions.IsAdminUser, )


class UserRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve a user or update user information.
    Accepts GET and PUT requests and the record id must be provided in the request """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #permission_classes = (permissions.IsAuthenticated, )

class PlanListCreate(generics.ListCreateAPIView):
    """ List and create Plan """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    #permission_classes = (permissions.IsAuthenticated, )


class PlanRetrieveUpdate(generics.RetrieveUpdateAPIView):
    """ Retrieve and update Plan information """
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    #permission_classes = (permissions.IsAuthenticated, )

class getVersion(APIView):
    """ Version """
    def get(self, request, format=None):
        return Response({"Version":"1.0.0"}, status=status.HTTP_200_OK)

class callHELP(APIView):
    """ HELP """
    def get(self, request, format=None):
        return Response({"HELP":"You don't need my help!"}, status=status.HTTP_200_OK)

class CardViewSet(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class CardToCardViewSet(generics.ListAPIView):
    queryset = CardToCard.objects.all()
    serializer_class = CardToCardSerializer

class PlaceNameListCreate(generics.ListCreateAPIView):
    """ List and create Place """
    queryset = PlaceName.objects.all()
    serializer_class = PlaceNameSerializer
    #permission_classes = (permissions.IsAuthenticated, )