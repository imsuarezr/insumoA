from django.db import models
from predio.models import *
from opciones.models import *

class NacimientosAgua(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	cantidad_corrientes = models.PositiveIntegerField(blank=True,null=True)
	protege_corrientes = models.ForeignKey(Booleanos,related_name='booleanos+',blank=True,null=True)
	cantidad_zonas_rurales = models.PositiveIntegerField(blank=True,null=True)
	forma_proteccion = models.ForeignKey(FormaProteccion,related_name='forma proteccion agua+',blank=True,null=True)

	def __unicode__(self):
		return self.predio.nombre_predio

class ViviendaUsos(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	agua_uso_domestico = models.ManyToManyField(AguaUsoDomestico,blank=True)
	agua_produccion = models.ManyToManyField(AguaProduccion,blank=True)
	sistema_succion_agua = models.ManyToManyField(SistemaSuccionAgua,blank=True)

	def __unicode__(self):
		return self.predio.nombre_predio




