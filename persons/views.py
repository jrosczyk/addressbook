from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

# Create your views here.

def index(request):
	persons = Person.objects.all()
	context = {'persons':persons}
	return render(request, 'persons/list.html', context)

def createPerson(request):
	form = PersonForm()

	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'form':form}
	return render(request, 'persons/create.html', context)

def editPerson(request, pk):
	person = Person.objects.get(id=pk)
	form = PersonForm(instance=person)

	if request.method == 'POST':
		form = PersonForm(request.POST, instance=person)
		if form.is_valid():
			form.save()
		return redirect('/')

	context = {'form':form}
	return render(request, 'persons/edit.html', context)

def deletePerson(request, pk):
	person = Person.objects.get(id=pk)

	if request.method == 'POST':
		person.delete()
		return redirect('/')

	context = {'person':person}
	return render(request, 'persons/delete.html', context)