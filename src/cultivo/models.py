from django.db import models
from predio.models import *


class TipoSiembra(models.Model):
	descripcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.descripcion

class Cultivo(models.Model):
	tipo_siembra = models.ForeignKey(TipoSiembra)
	nombre = models.CharField(max_length=100)
	cantidad = models.IntegerField()
	area_cultivada = models.CharField(max_length=100)
	area_cosechada = models.CharField(max_length=100)
	anio_establecimiento = models.DateField()
	rendimiento = models.CharField(max_length=100)
	predio = models.ForeignKey(Predio,related_name='predio')

	def __unicode__(self):
		return self.tipo_siembra_descripcion

class PlantacionForestal(models.Model):
	nombre_plantacion = models.CharField(max_length=100)
	descripcion = models.TextField()
	area_cultivada = models.CharField(max_length=100)
	area_cosechada = models.CharField(max_length=100)
	anio_establecimiento = models.DateField()
	rendimiento = models.CharField(max_length=100)
	predio = models.ForeignKey(Predio)
	tipo_siembra = models.ForeignKey(TipoSiembra,related_name='tipo_siembra')



class SistemasAgroforestales(models.Model):
	nombre_plantacion = models.CharField(max_length=100)
	descripcion = models.TextField()
	area_cultivada = models.CharField(max_length=100)
	area_cosechada = models.CharField(max_length=100)
	anio_establecimiento = models.DateField()
	rendimiento = models.CharField(max_length=100)
	predio = models.ForeignKey(Predio)
	tipo_siembra = models.ForeignKey(TipoSiembra,related_name='tipo_siembra')
