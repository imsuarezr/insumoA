from django import forms
from django.forms import ModelForm, CheckboxSelectMultiple
from .models import *

class FormProduccionLeche(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormProduccionLeche, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-mini'
			self.fields['a_quien_vende'].widget.attrs['class'] = 'input-medium'
			field.widget.attrs['min'] = 0
	class Meta():
		model = ProduccionLeche
		exclude = ('predio',)
		#widgets = {"a_quien_vende":CheckboxSelectMultiple(),}
		
class FormSuplementos(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormSuplementos, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-small'
			field.widget.attrs['placeholder'] = 'Valor'
			#sal blanca
			self.fields['sal_blanca_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['sal_blanca_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['sal_blanca_total'].widget.attrs['readonly'] = True
			#sal mineralizada
			self.fields['sal_mineralizada_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['sal_mineralizada_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['sal_mineralizada_total'].widget.attrs['readonly'] = True
			#premezca mineral
			self.fields['premezcla_mineral_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['premezcla_mineral_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['premezcla_mineral_total'].widget.attrs['readonly'] = True
			#azufre
			self.fields['azufre_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['azufre_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['azufre_total'].widget.attrs['readonly'] = True
			#concentrado comercial
			self.fields['concentrado_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['concentrado_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['concentrado_total'].widget.attrs['readonly'] = True
			#melaza
			self.fields['melaza_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['melaza_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['melaza_total'].widget.attrs['readonly'] = True
			#heno
			self.fields['heno_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['heno_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['heno_total'].widget.attrs['readonly'] = True
			#ensilaje
			self.fields['ensilaje_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['ensilaje_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['ensilaje_total'].widget.attrs['readonly'] = True
			#minvalue
			field.widget.attrs['min'] = 0

	class Meta():
		model = Suplementos
		exclude = ('predio',)
		

class FormInsumos(ModelForm):
	def __init__(self, *args, **kwargs):
		super(FormInsumos, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'input-small'
			field.widget.attrs['placeholder'] = 'Valor'
			#parasitos externos
			self.fields['parasitos_externos_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['parasitos_externos_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['parasitos_externos_total'].widget.attrs['readonly'] = True
			#alambre pua
			self.fields['alambre_pua_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['alambre_pua_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['alambre_pua_total'].widget.attrs['readonly'] = True
			#alambre cerca electrica
			self.fields['alambre_electrica_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['alambre_electrica_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['alambre_electrica_total'].widget.attrs['readonly'] = True
			#gallinaza compostada
			self.fields['gallinaza_compostada_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['gallinaza_compostada_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['gallinaza_compostada_total'].widget.attrs['readonly'] = True
			#servicios veterinarios
			self.fields['servicios_veterinarios_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['servicios_veterinarios_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['servicios_veterinarios_total'].widget.attrs['readonly'] = True
			#postes
			self.fields['postes_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['postes_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['postes_total'].widget.attrs['readonly'] = True
			#medicamentos
			self.fields['medicamentos_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['medicamentos_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['medicamentos_total'].widget.attrs['readonly'] = True
			#herbicidas
			self.fields['herbicidas_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['herbicidas_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['herbicidas_total'].widget.attrs['readonly'] = True
			#fertilizantes quimicos
			self.fields['fertilizantes_quimicos_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['fertilizantes_quimicos_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['fertilizantes_quimicos_total'].widget.attrs['readonly'] = True
			#fertilizantes organicos
			self.fields['fertilizantes_organicos_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['fertilizantes_organicos_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['fertilizantes_organicos_total'].widget.attrs['readonly'] = True
			#antiparasitarios
			self.fields['antiparasitarios_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['antiparasitarios_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['antiparasitarios_total'].widget.attrs['readonly'] = True
			#herramientas y accesorios
			self.fields['herramientas_accesorios_cantidad'].widget.attrs['placeholder'] = '(Kg)'
			self.fields['herramientas_accesorios_cantidad'].widget.attrs['class'] = 'input-mini'
			self.fields['herramientas_accesorios_total'].widget.attrs['readonly'] = True
			#minvalue
			field.widget.attrs['min'] = 0


	class Meta():
		model = Insumos
		exclude = ('predio',)

		