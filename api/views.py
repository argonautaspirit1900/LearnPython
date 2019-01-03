from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User
from challenges.models import Category,Challenge
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from tempfile import NamedTemporaryFile
from subprocess import Popen,PIPE,STDOUT
# Create your views here.

class GetOutput(APIView):
	permission_classes = []
	def post(self,request):
		if not request.data.get("source_code"):
			return Response({"error":True,"message":"source_code missing"})
		source_code = request.data["source_code"]
		output = None
		with NamedTemporaryFile(delete=False) as temp_file:
			for ch in source_code:
				temp_file.write(ch.encode("utf-8"))
			temp_file.flush()
			cmd = f"python3 {temp_file.name}"
			p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
			          stderr=STDOUT, close_fds=True)
			output = p.stdout.read()
		return Response({"output":output})

class UserViewSet(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer

class CategoryViewSet(ModelViewSet):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class ChallengeViewSet(ModelViewSet):
	queryset = Challenge.objects.all()
	serializer_class = ChallengeSerializer

