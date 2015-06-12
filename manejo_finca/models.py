from django.db import models
from predio.models import *
from opciones.models import *

class TipoOrdeno(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class SitemaReproduccion(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class TiposChequeo(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class MetodosDesmaleza(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class TipoPastoreo(models.Model):
	nombre = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nombre

class ManejoGeneral(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	tipo_ordeno = models.ForeignKey(TipoOrdeno,related_name='tipo ordeno+',blank=True,null=True)
	sistema_reproduccion = models.ForeignKey(SitemaReproduccion,related_name='sistema reproduccion+',blank=True,null=True)
	chequeos_reproductivos = models.ForeignKey(Booleanos,related_name='chequeos reproductivos+',blank=True,null=True)
	tipos_chequeo = models.ForeignKey(TiposChequeo,related_name='tipo chequeo+',blank=True,null=True)
	cria_terreno_macho = models.ForeignKey(Booleanos,related_name='cria terreno macho+',blank=True,null=True)
	limite_edad_crianza = models.PositiveIntegerField(blank=True,null=True)
	arrienda_potreros = models.ForeignKey(Booleanos,related_name='arrienda potreros+',blank=True,null=True)
	numero_hectareas_arrienda = models.DecimalField(max_digits=4,decimal_places=2,blank=True,null=True)
	cuanto_paga_por_animal = models.PositiveIntegerField(blank=True,null=True)
	cuanto_paga_por_hectarea = models.PositiveIntegerField(blank=True,null=True)
	#potreros
	cantidad_potreros_finca = models.PositiveIntegerField(blank=True,null=True)
	tipo_pastoreo = models.ForeignKey(TipoPastoreo,blank=True,null=True)
	dias_descanso_potrero_epocas_lluvia = models.PositiveIntegerField(blank=True,null=True)
	dias_ocupacion_potrero_epocas_lluvia = models.PositiveIntegerField(blank=True,null=True)
	dias_descanso_potrero_epocas_sequia = models.PositiveIntegerField(blank=True,null=True)
	dias_ocupacion_potrero_epocas_sequia = models.PositiveIntegerField(blank=True,null=True)
	dias_anio_limpieza_potrero = models.PositiveIntegerField(blank=True,null=True)
	metodo_desmalezar = models.ManyToManyField(MetodosDesmaleza,related_name='metodos desmaleza+',blank=True)

	def __unicode__(self):
		return self.predio.nombre_predio

class EnfermedadesFrecuentes(models.Model):
	nombre = models.CharField(max_length=100)
	def __unicode__(self):
		return self.nombre

class LaboresAnimales(models.Model):
	nombre = models.CharField(max_length=100)
	def __unicode__(self):
		return self.nombre

class Vacunas(models.Model):
	nombre = models.CharField(max_length=100)
	def __unicode__(self):
		return self.nombre

class Enfermedades(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	enfermedades_frecuentes = models.ManyToManyField(EnfermedadesFrecuentes,blank=True)
	labores_animales = models.ManyToManyField(LaboresAnimales,blank=True)
	vacunas = models.ManyToManyField(Vacunas,blank=True)

	def __unicode__(self):
		return self.predio.nombre_predio



