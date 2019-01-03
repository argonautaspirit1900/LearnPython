from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=300)

class Challenge(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	title = models.CharField(max_length=500)
	description = models.TextField()
	expected_output = models.TextField()
