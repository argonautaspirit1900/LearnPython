from rest_framework import serializers
from django.contrib.auth.models import User
from challenges.models import Category,Challenge

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		exclude = []

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		exclude = []

class ChallengeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Challenge
		exclude = []
