from django import forms
from django.forms import ModelForm
from .models import *


class FormInventarioHembras(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormInventarioHembras, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-mini'
			field.widget.attrs['placeholder'] = 'Has'
			#readonly
			self.fields['vacas_paridas_totales'].widget.attrs['readonly'] = True
			self.fields['vacas_horras_totales'].widget.attrs['readonly'] = True
			self.fields['vacas_23_totales'].widget.attrs['readonly'] = True
			self.fields['vacas_12_totales'].widget.attrs['readonly'] = True
			self.fields['vacas_menores_totales'].widget.attrs['readonly'] = True
			self.fields['vacas_descarte_totales'].widget.attrs['readonly'] = True
	class Meta():
		model = GanadoHembras
		exclude = ('predio',)
		
class FormInventarioMachos(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormInventarioMachos, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-mini'
			field.widget.attrs['placeholder'] = 'Has'
			#readonly
			self.fields['toros_totales'].widget.attrs['readonly'] = True
			self.fields['machos_mayores_3_anios_totales'].widget.attrs['readonly'] = True
			self.fields['machos_2_a_3_anios_totales'].widget.attrs['readonly'] = True
			self.fields['machos_1_a_2_anios_totales'].widget.attrs['readonly'] = True
			self.fields['machos_menores_1_anio_totales'].widget.attrs['readonly'] = True
			self.fields['bueyes_totales'].widget.attrs['readonly'] = True
	class Meta():
		model = GanadoMachos
		exclude = ("predio",)
		
class FormOtrasEspecies(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormOtrasEspecies, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-mini'
			field.widget.attrs['placeholder'] = 'Has'
			#readonly
			self.fields['caballares_totales'].widget.attrs['readonly'] = True
			self.fields['mulares_totales'].widget.attrs['readonly'] = True
			self.fields['cochino_sabanero_totales'].widget.attrs['readonly'] = True
			self.fields['cerdos_confinamiento_totales'].widget.attrs['readonly'] = True
			self.fields['gallina_encasetada_totales'].widget.attrs['readonly'] = True
			self.fields['pollos_engorde_totales'].widget.attrs['readonly'] = True
			self.fields['aves_traspatio_totales'].widget.attrs['readonly'] = True
			self.fields['ovinos_totales'].widget.attrs['readonly'] = True
			self.fields['caprinos_totales'].widget.attrs['readonly'] = True
			self.fields['peces_totales'].widget.attrs['readonly'] = True
			self.fields['buffalos_totales'].widget.attrs['readonly'] = True
	class Meta():
		model = OtrasEspecies
		exclude = ("predio",)
		

class FormDobleProposito(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormDobleProposito, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-mini'
			self.fields['ganancia_diaria_peso_levante'].widget.attrs['readonly'] = True
			self.fields['ganancia_diaria_peso_ceba'].widget.attrs['readonly'] = True
			field.widget.attrs['min'] = 0
	class Meta():
		model = ParametroProductivo
		exclude = ("predio",)
		




		