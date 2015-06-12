from django import forms
from django.forms import ModelForm
from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput, EmailInput, DateInput, Textarea
from .models import *

class FormNacimientosAgua(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormNacimientosAgua, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			self.fields['forma_proteccion'].widget.attrs['class'] = 'input-large'
	class Meta():
		model = NacimientosAgua
		exclude = ('predio',)

class FormUsosAgua(ModelForm):
	class Meta():
		model = ViviendaUsos
		exclude = ('predio',)


