from django import forms
from django.forms import ModelForm
from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput, EmailInput, DateInput, Textarea
from .models import *

class FormPastoreo(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormPastoreo, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['placeholder'] = 'Has'
			field.widget.attrs['class'] = 'input-mini'
			

	class Meta():
		model = Pastoreo
		exclude = ('predio',)
		
class FormBancosForraje(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormBancosForraje, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['placeholder'] = 'Has'
			field.widget.attrs['class'] = 'input-mini'
			field.widget.attrs['min'] = 0
	class Meta():
		model = BancosForraje
		exclude = ('predio',)
		
		
class FormCultivosAgricolas(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormCultivosAgricolas, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['placeholder'] = 'Has'
			field.widget.attrs['class'] = 'input-mini'
			field.widget.attrs['min'] = 0
	class Meta():
		model = CultivoAgricolasYForestales
		exclude = ('predio',)
		


		
#edit

class PastoreoEditForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PastoreoEditForm, self).__init__(*args, **kwargs)
	class Meta:
		model = Pastoreo
		exclude = ('predio',)

class BancosForrajeEditForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(BancosForrajeEditForm, self).__init__(*args, **kwargs)
	class Meta:
		model = BancosForraje
		exclude = ('predio',)
"""
class CultivoAgricolaEditForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(CultivoAgricolaEditForm, self).__init__(*args, **kwargs)
	class Meta:
		model = CultivoAgricola
		exclude = ('predio',)
"""



