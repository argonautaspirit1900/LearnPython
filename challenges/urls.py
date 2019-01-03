from django.urls import path
from . import views

urlpatterns = [
	path("solve/<int:pk>",views.solve_challenge,name="solve_challenge"),
]