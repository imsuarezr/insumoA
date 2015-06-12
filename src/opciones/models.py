from django.db import models


class TipoIdentificacion(models.Model):
	opcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.opcion

class EstadoCivil(models.Model):
	opcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.opcion		

class RegimenSalud(models.Model):
	opcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.opcion

class Sisben(models.Model):
	opcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.opcion

class Genero(models.Model):
	opcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.opcion


class Booleanos(models.Model):
	opcion = models.CharField(max_length=2)

	def __unicode__(self):
		return self.opcion

class Cubierta(models.Model):
	opcion = models.CharField(max_length=30)

	def __unicode__(self):
		return self.opcion

class TipoConstruccion(models.Model):
	opcion = models.CharField(max_length=30)

	def __unicode__(self):
		return self.opcion

class BMR(models.Model):
	opcion = models.CharField(max_length=30)

	def __unicode__(self):
		return self.opcion


class FuenteEnergia(models.Model):
	opcion = models.CharField(max_length=30)

	def __unicode__(self):
		return self.opcion


class FuenteEnergiaPreparacionAlimentos(models.Model):
	opcion = models.CharField(max_length=30)

	def __unicode__(self):
		return self.opcion


class FormaProteccion(models.Model):
	opcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.opcion

class AguaUsoDomestico(models.Model):
	opcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.opcion

class AguaProduccion(models.Model):
	opcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.opcion

class SistemaSuccionAgua(models.Model):
	opcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.opcion

class TipoSiembra(models.Model):
	opcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.opcion

class SistemaReproduccion(models.Model):
	opcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.opcion

class AtractivoEcoturismo(models.Model):
	opcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.opcion


class ActividadEcoturismo(models.Model):
	opcion = models.CharField(max_length=100)

	def __unicode__(self):
		return self.opcion



