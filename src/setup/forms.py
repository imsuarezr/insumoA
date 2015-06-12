from django import forms
from django.forms import ModelForm
from setup.views import *
from predio.models import *


class BuscarForm(forms.ModelForm):
	class Meta:
		model = InfoPredioGeneral
		fields = '__all__'


class PersonaEditForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(PersonaEditForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control' ' width=50px'
	class Meta:
		model = InfoPredioGeneral
		fields = '__all__'


class FormCreditoPredio(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormCreditoPredio, self).__init__(*args, **kwargs)
	class Meta():
		model = CreditoPredio
		exclude = ('predio',)
		