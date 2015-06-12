from django import forms
from django.forms import ModelForm
from django.forms import ModelForm, TextInput, Select, CheckboxInput, SelectMultiple, CheckboxSelectMultiple
from .models import *

class FormAgroecoturismo(ModelForm):
	class Meta():
		model = Agroecoturismo
		exclude = ("predio",)

