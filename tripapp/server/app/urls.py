from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserList.as_view()),
    path('create-users/', UserCreate.as_view()),
    path('users/<pk>/', UserRetrieveUpdate.as_view()),

    path('plans/', PlanListCreate.as_view()),
    path('plans/<pk>/', PlanRetrieveUpdate.as_view()),

    path('version/', getVersion.as_view()),

    path('help/', callHELP.as_view()),

    path('cards/', CardViewSet.as_view()),

]
