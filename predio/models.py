from django.db import models
from opciones.models import *
from django.contrib.auth.models import User
from ubicaciones.models import *
from django.core.exceptions import *
from django.core.validators import MaxValueValidator, MinValueValidator


class DocumentoAcreditacion(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class MedioTransporte(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class OrigenCredito(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class UsoPrincipalCredito(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre

class TipoIncentivo(models.Model):
	nombre = models.CharField(max_length=100)

	def __unicode__(self):
		return self.nombre


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)



class InfoPredioGeneral(models.Model):
	user = models.ForeignKey(User)
	fecha = models.DateField(auto_now=True)
	pais = models.ForeignKey(Pais,related_name='pais+',blank=True,null=True)
	departamento = models.ForeignKey(Departamento,related_name='departamento+',blank=True,null=True)
	municipio = models.ForeignKey(Municipio,related_name='municipio+',blank=True,null=True)
	centro_poblado = models.ForeignKey(Booleanos,related_name='centro poblado+',blank=True,null=True)
	zona = models.ForeignKey(Zona,related_name='zona+',blank=True,null=True)
	corregimiento = models.ForeignKey(Corregimiento,related_name='corregimiento+',blank=True,null=True)
	vereda = models.ForeignKey(Vereda,related_name='vereda+',blank=True,null=True)
	nombre_predio = models.CharField(max_length=30)
	coordenada_n = models.FloatField('Latitude',blank=True,null=True)
	coordenada_w = models.FloatField('Longitude',blank=True,null=True)
	ext_total = models.FloatField (blank=True,null=True)
	area_arrendamiento = models.FloatField (blank=True,null=True)
	altitud = models.PositiveIntegerField(blank=True,null=True)
	precipitacion = models.PositiveIntegerField(blank=True,null=True)
	km_cabecera_mpal = models.FloatField (blank=True,null=True)
	acceso_predio_anio = models.ForeignKey(BMR,blank=True,null=True)
	medio_transporte_predio = models.ForeignKey(MedioTransporte,blank=True,null=True)
	tenencia_finca = models.PositiveIntegerField(blank=True,null=True)
	utiliza_sabanas_comunales = models.ForeignKey(Booleanos,related_name='sabanas comunales+',blank=True,null=True)
	viven_producido = models.ForeignKey(Booleanos,related_name='viven del producido+',blank=True,null=True)
	documento_acreditacion_propiedad = models.ForeignKey(DocumentoAcreditacion,blank=True,null=True,related_name='documento_acreditacio_propiedad+')
	numero_documento_acreditacion_inmueble = models.CharField(max_length=100,blank=True,null=True)
	fecha_expedicion_acreditacion_inmueble = models.DateField(blank=True,null=True)
	lugar_expedicion_acreditacion_inmueble =  models.CharField(max_length=100,blank=True,null=True)
	matricula_inmobiliaria = models.CharField(max_length=100,blank=True,null=True)
	cedula_catastral_acreditacion_inmueble = models.CharField(max_length=100,blank=True,null=True)
	documento_acreditacion_tierra = models.ForeignKey(DocumentoAcreditacion,blank=True,null=True,related_name='documento_acreditacio_tierra+')
	numero_documento_acreditacion_tierra = models.CharField(max_length=100,blank=True,null=True)
	fecha_expedicion_acreditacion_tierra = models.DateField(blank=True,null=True)
	lugar_expedicion_acreditacion_tierra = models.CharField(max_length=100,blank=True,null=True)
	matricula_inmobiliaria_acreditacion_tierra = models.CharField(max_length=100,blank=True,null=True)
	cedula_catastral_acreditacion_tierra = models.CharField(max_length=100,blank=True,null=True)

	def __str__(self):
		return self.nombre_predio


"""	
	total_area_pastoreo = models.IntegerField(blank=True,null=True)
	total_banco_forraje = models.IntegerField(blank=True,null=True)
	total_bosque = models.IntegerField(blank=True,null=True)
	total_cultivo = models.IntegerField(blank=True,null=True)
	total_plantacion_forestal = models.IntegerField(blank=True,null=True)
	total_sistema_agroforestal = models.IntegerField(blank=True,null=True)
	total_uso_suelo = models.IntegerField(blank=True,null=True)
"""


class CantidadCreditoPredio(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	cantidad_credito = models.PositiveIntegerField(blank=True,null=True)

	def __unicode__(self):
		return self.predio.nombre_predio


class CreditoPredio(models.Model):
	TIPO_CUOTA_CHOICES = (
		('Mensual', 'Mensual'),
   		('Semestral', 'Semestral'),
	)
	POSEE_INCENTIVO_CHOICES = (
		('Si', 'Si'),
   		('No', 'No'),
	)		
	predio = models.ForeignKey(InfoPredioGeneral)
	consecutivo = models.IntegerField(null=True)
	origen_credito = models.ForeignKey(OrigenCredito,max_length=100,blank=True,null=True)
	lugar_expedicion = models.CharField(max_length=100,blank=True,null=True)
	pago_cuota = models.PositiveIntegerField(blank=True,null=True)
	tipo_cuota = models.CharField(max_length=30,blank=True,null=True,choices=TIPO_CUOTA_CHOICES)
	uso_principal = models.ForeignKey(UsoPrincipalCredito,max_length=100,blank=True,null=True)
	posee_incentivo = models.CharField(max_length=2,blank=True,null=True,choices=POSEE_INCENTIVO_CHOICES)
	tipo_incentivo = models.ForeignKey(TipoIncentivo,max_length=100,blank=True,null=True)
	ingresos_externos = models.CharField(max_length=2,blank=True,null=True,choices=POSEE_INCENTIVO_CHOICES)
	posee_subsidio = models.CharField(max_length=2,blank=True,null=True,choices=POSEE_INCENTIVO_CHOICES)

	def __unicode__(self):
		return self.predio.nombre_predio

	class Meta:
		ordering = ["pk"]


class ViviendaPredio(models.Model):

	predio = models.ForeignKey(InfoPredioGeneral)
	posee_vivienda = models.ForeignKey(Booleanos,related_name='booleanos+',blank=True,null=True)
	cubierta = models.ForeignKey(Cubierta,related_name='cubierta+',blank=True,null=True)
	tipo_construccion = models.ForeignKey(TipoConstruccion,related_name='tipo construccion+',blank=True,null=True)
	estado_saneamiento = models.ForeignKey(BMR,related_name='bueno malo regular+',blank=True,null=True)
	bateria_sanitaria = models.ForeignKey(Booleanos,related_name='booleanos+',blank=True,null=True)
	energia_electrica = models.ForeignKey(Booleanos,related_name='booleanos+',blank=True,null=True)
	energia_alternativa = models.ForeignKey(Booleanos,related_name='booleanos+',blank=True,null=True)
	fuente_energia = models.ForeignKey(FuenteEnergia,related_name='fuente energia+',blank=True,null=True)
	energia_preparacion_alimentos = models.ManyToManyField(FuenteEnergiaPreparacionAlimentos,related_name='fuente energia+',blank=True)

	def __unicode__(self):
		return self.predio.nombre_predio
