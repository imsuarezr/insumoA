from django.db import models

class Pais(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Departamento(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Municipio(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Zona(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Corregimiento(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class Vereda(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

		