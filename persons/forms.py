from django import forms
from django.forms import ModelForm

from .models import *


class PersonForm(forms.ModelForm):

	class Meta:
		model = Person
		# fields = '__all__'
		fields = ['first_name', 'last_name', 'email', 'phone']
		widgets = {
	        'first_name': forms.TextInput(
				attrs={
					'class': 'form-control'
				}
			),
			'last_name': forms.TextInput(
				attrs={
					'class': 'form-control'
				}
			),
			'email': forms.EmailInput(
				attrs={
					'class': 'form-control'
				}
			),
			'phone': forms.TextInput(
				attrs={
					'class': 'form-control'
				}
			),
		}