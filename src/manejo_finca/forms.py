from django import forms
from django.forms import ModelForm
from .models import *

class FormManejoGeneral(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormManejoGeneral, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-small'
			self.fields['metodo_desmalezar'].widget.attrs['class'] = 'input-large'
	class Meta():
		model = ManejoGeneral
		exclude = ("predio",)

class FormEnfermedades(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormEnfermedades, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-large'
	class Meta():
		model = Enfermedades
		exclude = ("predio",)
		

