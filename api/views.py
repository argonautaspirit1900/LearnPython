from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from django.contrib.auth.models import User
from challenges.models import Category,Challenge

# Create your views here.

class UserViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class CategoryViewSet(ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class ChallengeViewSet(ModelViewSet):
	queryset = Challenge.objects.all()
	serializer_class = ChallengeSerializer

