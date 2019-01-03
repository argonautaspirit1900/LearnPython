from django.shortcuts import render,get_object_or_404
from .models import Challenge

# Create your views here.

def solve_challenge(request,pk):
	challenge = get_object_or_404(Challenge,pk=pk)
	context = {"challenge":challenge}
	return render(request,"challenges/solve_challenge.html",context)