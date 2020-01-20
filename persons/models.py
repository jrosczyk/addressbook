from django.db import models
from phone_field import PhoneField

# Create your models here.

class Person(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=254)
	phone = PhoneField(help_text='Contact phone number')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.first_name + ' ' + self.last_name