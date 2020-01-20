from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="list"),
	path('create/', views.createPerson, name="create"),
	path('edit/<str:pk>/', views.editPerson, name="edit"),
	path('delete/<str:pk>/', views.deletePerson, name="delete"),
]