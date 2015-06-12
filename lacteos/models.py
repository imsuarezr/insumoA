from django.db import models
from predio.models import InfoPredioGeneral


class Comprador(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class ProduccionLeche(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	total_producido_litro_dia = models.FloatField (blank=True,null=True,default=0)
	cantidad_destinada_productos_lacteos = models.FloatField (blank=True,null=True,default=0)
	cantidad_destinada_autoconsumo_dia = models.FloatField (blank=True,null=True,default=0)
	precio_litro_leche = models.FloatField (blank=True,null=True,default=0)
	promedio_vacas_ordenadas_dia = models.FloatField (blank=True,null=True,default=0)
	mantequilla = models.FloatField (blank=True,null=True,default=0)
	yogurth = models.FloatField (blank=True,null=True,default=0)
	kumis = models.FloatField (blank=True,null=True,default=0)
	dulces = models.FloatField (blank=True,null=True,default=0)
	queso_de_mano = models.FloatField (blank=True,null=True,default=0)
	queso_cuajada = models.FloatField (blank=True,null=True,default=0)
	queso_prensado = models.FloatField (blank=True,null=True,default=0)
	queso_maduro = models.FloatField (blank=True,null=True,default=0)
	a_quien_vende = models.ManyToManyField(Comprador,blank=True)

	def __unicode__(self):
		return self.predio.nombre_predio

class Suplementos(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	#sal blanca
	sal_blanca_cantidad = models.FloatField (blank=True,null=True,default=0)
	sal_blanca_valor = models.FloatField (blank=True,null=True,default=0)
	sal_blanca_total = models.FloatField (blank=True,null=True,default=0)
	#sal mineralizada
	sal_mineralizada_cantidad = models.FloatField (blank=True,null=True,default=0)
	sal_mineralizada_valor = models.FloatField (blank=True,null=True,default=0)
	sal_mineralizada_total = models.FloatField (blank=True,null=True,default=0)
	#premezcla mineral
	premezcla_mineral_cantidad = models.FloatField (blank=True,null=True,default=0)
	premezcla_mineral_valor = models.FloatField (blank=True,null=True,default=0)
	premezcla_mineral_total = models.FloatField (blank=True,null=True,default=0)
	#azufre
	azufre_cantidad = models.FloatField (blank=True,null=True,default=0)
	azufre_valor = models.FloatField (blank=True,null=True,default=0)
	azufre_total = models.FloatField (blank=True,null=True,default=0)
	#concentrado comercial
	concentrado_cantidad = models.FloatField (blank=True,null=True,default=0)
	concentrado_valor = models.FloatField (blank=True,null=True,default=0)
	concentrado_total = models.FloatField (blank=True,null=True,default=0)
	#melaza
	melaza_cantidad = models.FloatField (blank=True,null=True,default=0)
	melaza_valor = models.FloatField (blank=True,null=True,default=0)
	melaza_total = models.FloatField (blank=True,null=True,default=0)
	#heno
	heno_cantidad = models.FloatField (blank=True,null=True,default=0)
	heno_valor = models.FloatField (blank=True,null=True,default=0)
	heno_total = models.FloatField (blank=True,null=True,default=0)
	#ensilaje
	ensilaje_cantidad = models.FloatField (blank=True,null=True,default=0)
	ensilaje_valor = models.FloatField (blank=True,null=True,default=0)
	ensilaje_total = models.FloatField (blank=True,null=True,default=0)

	def __unicode__(self):
		return self.predio.nombre_predio

class Insumos(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	#parasitos externos
	parasitos_externos_cantidad = models.FloatField (blank=True,null=True,default=0)
	parasitos_externos_valor = models.FloatField (blank=True,null=True,default=0)
	parasitos_externos_total = models.FloatField (blank=True,null=True,default=0)
	#alambre pua
	alambre_pua_cantidad = models.FloatField (blank=True,null=True,default=0)
	alambre_pua_valor = models.FloatField (blank=True,null=True,default=0)
	alambre_pua_total = models.FloatField (blank=True,null=True,default=0)
	#alambre cerca electrica
	alambre_electrica_cantidad = models.FloatField (blank=True,null=True,default=0)
	alambre_electrica_valor = models.FloatField (blank=True,null=True,default=0)
	alambre_electrica_total = models.FloatField (blank=True,null=True,default=0)
	#gallinaza compostada
	gallinaza_compostada_cantidad = models.FloatField (blank=True,null=True,default=0)
	gallinaza_compostada_valor = models.FloatField (blank=True,null=True,default=0)
	gallinaza_compostada_total = models.FloatField (blank=True,null=True,default=0)
	#servicios veterinaios
	servicios_veterinarios_cantidad = models.FloatField (blank=True,null=True,default=0)
	servicios_veterinarios_valor = models.FloatField (blank=True,null=True,default=0)
	servicios_veterinarios_total = models.FloatField (blank=True,null=True,default=0)
	#postes
	postes_cantidad = models.FloatField (blank=True,null=True,default=0)
	postes_valor = models.FloatField (blank=True,null=True,default=0)
	postes_total = models.FloatField (blank=True,null=True,default=0)
	#medicamentos
	medicamentos_cantidad = models.FloatField (blank=True,null=True,default=0)
	medicamentos_valor = models.FloatField (blank=True,null=True,default=0)
	medicamentos_total = models.FloatField (blank=True,null=True,default=0)
	#herbicidas
	herbicidas_cantidad = models.FloatField (blank=True,null=True,default=0)
	herbicidas_valor = models.FloatField (blank=True,null=True,default=0)
	herbicidas_total = models.FloatField (blank=True,null=True,default=0)
	#fertilizantes quimicos
	fertilizantes_quimicos_cantidad = models.FloatField (blank=True,null=True,default=0)
	fertilizantes_quimicos_valor = models.FloatField (blank=True,null=True,default=0)
	fertilizantes_quimicos_total = models.FloatField (blank=True,null=True,default=0)
	#fertilizantes organicos
	fertilizantes_organicos_cantidad = models.FloatField (blank=True,null=True,default=0)
	fertilizantes_organicos_valor = models.FloatField (blank=True,null=True,default=0)
	fertilizantes_organicos_total = models.FloatField (blank=True,null=True,default=0)
	#antiparasitarios
	antiparasitarios_cantidad = models.FloatField (blank=True,null=True,default=0)
	antiparasitarios_valor = models.FloatField (blank=True,null=True,default=0)
	antiparasitarios_total = models.FloatField (blank=True,null=True,default=0)
	#herramientas y accesorios
	herramientas_accesorios_cantidad = models.FloatField (blank=True,null=True,default=0)
	herramientas_accesorios_valor = models.FloatField (blank=True,null=True,default=0)
	herramientas_accesorios_total = models.FloatField (blank=True,null=True,default=0)

	def __unicode__(self):
		return self.predio.nombre_predio





