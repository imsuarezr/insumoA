from django import forms
from django.forms import ModelForm, widgets, CheckboxSelectMultiple, Select
from .models import *
from .views import *

class FormInfoGeneralPredio(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormInfoGeneralPredio, self).__init__(*args, **kwargs)
		self.initial['departamento'] = "1"
		self.fields['departamento'].initial = "1"
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-medium'
			self.fields['municipio'].widget.attrs['class'] = 'input-small'
			self.fields['centro_poblado'].widget.attrs['class'] = 'input-medium'
			self.fields['zona'].widget.attrs['class'] = 'input-small'
			self.fields['ext_total'].widget.attrs['min'] = 0
			self.fields['area_arrendamiento'].widget.attrs['min'] = 0
			self.fields['km_cabecera_mpal'].widget.attrs['min'] = 0

	def clean(self):
		cleaned_data = self.cleaned_data
		predio = cleaned_data.get('nombre_predio')

		if not predio:
			raise forms.ValidationError("Debe especificar un Predio")
		else:
			self.cleaned_data['nombre_predio'] = predio
		return super(FormInfoGeneralPredio,self).clean()

	class Meta():
		model = InfoPredioGeneral
		exclude = ('user',)
		#widgets = {
        #    'fecha_expedicion_acreditacion_inmueble' : forms.DateInput(attrs={'type':'date'}),
        #    'fecha_expedicion_acreditacion_tierra' : forms.DateInput(attrs={'type':'date'}),
        #}

		


class FormCantidadCreditoPredio(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormCantidadCreditoPredio, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-medium'
			#self.fields['tipo_incentivo'].widget.attrs['readonly'] = True
	class Meta():
		model = CantidadCreditoPredio
		exclude = ('predio',)


class FormCreditoPredio(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormCreditoPredio, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-medium'
			#self.fields['tipo_incentivo'].widget.attrs['readonly'] = True
	class Meta():
		model = CreditoPredio
		exclude = ('predio','consecutivo')
		

class FormViviendaPreio(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormViviendaPreio, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-medium'
	class Meta():
		model = ViviendaPredio
		exclude = ('predio',)
		#widgets = {"energia_preparacion_alimentos":CheckboxSelectMultiple(),}

