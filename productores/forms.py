from django import forms
from django.forms import ModelForm
from django.forms import ModelForm, TextInput, Textarea, Select, NumberInput, EmailInput, DateInput, Textarea
from .models import *
from productores.views import *

class FormPropietario(ModelForm):

	def prop_admin(self,predio_id):
		x = Administrador.objects.filter(predio_id=predio_id).latest('id')
		if x:
			x.delete()
			admin = Administrador.objects.get_or_create(predio_id=predio_id,**self.cleaned_data)
		else:
			admin = Administrador.objects.get_or_create(predio_id=predio_id,**self.cleaned_data)

	def __init__(self, *args, **kwargs):
		super(FormPropietario, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-medium'
			self.fields['primer_nombre'].widget.attrs['required'] = True
	class Meta():
		model = Propietario
		exclude = ("predio",'rol',)
		widgets = {
            'fecha_nacimiento' : forms.DateInput(attrs={'type':'date'}),
        }
		
class FormAdministrador(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormAdministrador, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-medium'
			self.fields['primer_nombre'].widget.attrs['required'] = True
	class Meta():
		model = Administrador
		exclude = ("predio",'rol')
		widgets = {
            'fecha_nacimiento' : forms.DateInput(attrs={'type':'date'}),
        }
		

class FormEncargado(ModelForm):
	def prop_admin_enc(self,predio_id):
		x = Administrador.objects.filter(predio_id=predio_id).latest('id')
		y = Propietario.objects.filter(predio_id=predio_id).latest('id')
		if x or y:
			x.delete()
			y.delete()
			admin = Administrador.objects.get_or_create(predio_id=predio_id,**self.cleaned_data)
			prop = Propietario.objects.get_or_create(predio_id=predio_id,**self.cleaned_data)
		else:
			admin = Administrador.objects.get_or_create(predio_id=predio_id,**self.cleaned_data)
			prop = Propietario.objects.get_or_create(predio_id=predio_id,**self.cleaned_data)
	
	
	def __init__(self, *args, **kwargs):
		super(FormEncargado, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-medium'
			self.fields['primer_nombre'].widget.attrs['required'] = True
	class Meta():
		model = Encargado
		exclude = ("predio",'rol',)
		widgets = {
            'fecha_nacimiento' : forms.DateInput(attrs={'type':'date'}),
        }

	

class FormHabitantes(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormHabitantes, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-mini'
			#required
			self.fields['cantidad_ninos'].widget.attrs['required'] = True
			self.fields['cantidad_ninas'].widget.attrs['required'] = True
			self.fields['cantidad_adultos_masculino'].widget.attrs['required'] = True
			self.fields['cantidad_adultos_femenino'].widget.attrs['required'] = True
			self.fields['cantidad_adultos_mayores_masculino'].widget.attrs['required'] = True
			self.fields['cantidad_adultos_mayores_femenino'].widget.attrs['required'] = True
			#read only
			self.fields['total_ninos'].widget.attrs['readonly'] = True
			self.fields['total_adultos'].widget.attrs['readonly'] = True
			self.fields['total_adultos_mayores'].widget.attrs['readonly'] = True
			self.fields['cantidad_habitantes'].widget.attrs['readonly'] = True
	class Meta():
		model = Habitantes
		exclude = ("predio",)
		
