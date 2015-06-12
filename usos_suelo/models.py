from django.db import models
from predio.models import *
from opciones.models import *

class Pastoreo(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral,related_name='predio')
	pasturas_nativas_sin_arboles = models.FloatField (blank=True,null=True,default=0)
	pasturas_introducidas_sin_arboles = models.FloatField (blank=True,null=True,default=0)
	arboles_dispersos_en_potreros = models.FloatField (blank=True,null=True,default=0)
	franjas_dobles_arboles_en_potreros = models.FloatField (blank=True,null=True,default=0)
	cercas_vivas = models.FloatField (blank=True,null=True,default=0)
	sistema_silvopastoril_intensivo = models.FloatField (blank=True,null=True,default=0)
	sistema_silvopastoril_intensivo_con_maderables = models.FloatField (blank=True,null=True,default=0)


	def __unicode__(self):
		return self.predio.nombre_predio


class BancosForraje(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral,related_name='nombre del predio+')
	bancos_energia = models.FloatField (blank=True,null=True,default=0)
	bancos_proteina = models.FloatField (blank=True,null=True,default=0)
	bancos_mixtos = models.FloatField (blank=True,null=True,default=0)

	def __unicode__(self):
		return self.predio.nombre_predio


class CultivoAgricolasYForestales(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	maiz = models.FloatField (blank=True,null=True,default=0)
	platano = models.FloatField (blank=True,null=True,default=0)
	cafe = models.FloatField (blank=True,null=True,default=0)
	eucalipto = models.FloatField (blank=True,null=True,default=0)
	pino = models.FloatField (blank=True,null=True,default=0)
	teca = models.FloatField (blank=True,null=True,default=0)
	maiz_con_platano = models.FloatField (blank=True,null=True,default=0)
	platano_con_cacao = models.FloatField (blank=True,null=True,default=0)
	cafe_con_platano = models.FloatField (blank=True,null=True,default=0)
	teca_mas_melina = models.FloatField (blank=True,null=True,default=0)
	pardillo_mas_tolua = models.FloatField (blank=True,null=True,default=0)

	def __unicode__(self):
		return self.predio.nombre_predio






