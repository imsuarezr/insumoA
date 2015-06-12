from django.db import models
from predio.models import InfoPredioGeneral

class GanadoHembras(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	vacas_paridas_propias = models.PositiveIntegerField(blank=True,null=True,default=0)
	vacas_paridas_ajenas = models.PositiveIntegerField(blank=True,null=True,default=0) 
	vacas_paridas_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#horras
	vacas_horras_propias = models.PositiveIntegerField(blank=True,null=True,default=0)
	vacas_horras_ajenas = models.PositiveIntegerField(blank=True,null=True,default=0)
	vacas_horras_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#dos a tres anios
	vacas_23_propias = models.PositiveIntegerField(blank=True,null=True,default=0)
	vacas_23_ajenas = models.PositiveIntegerField(blank=True,null=True,default=0)
	vacas_23_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#uno a dos anios	
	vacas_12_propias = models.PositiveIntegerField(blank=True,null=True,default=0)
	vacas_12_ajenas = models.PositiveIntegerField(blank=True,null=True,default=0)
	vacas_12_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#menores	
	vacas_menores_propias = models.PositiveIntegerField(blank=True,null=True,default=0)
	vacas_menores_ajenas = models.PositiveIntegerField(blank=True,null=True,default=0)
	vacas_menores_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#saca
	vacas_descarte_propias = models.PositiveIntegerField(blank=True,null=True,default=0)
	vacas_descarte_ajenas = models.PositiveIntegerField(blank=True,null=True,default=0)
	vacas_descarte_totales = models.PositiveIntegerField(blank=True,null=True,default=0)

	def __unicode__(self):
		return self.predio.nombre_predio


class GanadoMachos(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	#toros
	toros_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	toros_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	toros_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#machos mayores a 3 anios
	machos_mayores_3_anios_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	machos_mayores_3_anios_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	machos_mayores_3_anios_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#machos de 2 a 3 anios
	machos_2_a_3_anios_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	machos_2_a_3_anios_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	machos_2_a_3_anios_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#machos de 1 a 2 anios 
	machos_1_a_2_anios_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	machos_1_a_2_anios_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	machos_1_a_2_anios_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#machos menores a 1 anio
	machos_menores_1_anio_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	machos_menores_1_anio_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	machos_menores_1_anio_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#bueyes
	bueyes_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	bueyes_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	bueyes_totales = models.PositiveIntegerField(blank=True,null=True,default=0)

	def __unicode__(self):
		return self.predio.nombre_predio

class OtrasEspecies(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	#CABALLERES
	caballares_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	caballares_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	caballares_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#MULARES
	mulares_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	mulares_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	mulares_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#COCHINO SABANERO
	cochino_sabanero_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	cochino_sabanero_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	cochino_sabanero_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#CERDOS EN CONFINAMIENTO
	cerdos_confinamiento_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	cerdos_confinamiento_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	cerdos_confinamiento_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#GALLINA ENCASETADA
	gallina_encasetada_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	gallina_encasetada_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	gallina_encasetada_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#POLLOS ENGORDE
	pollos_engorde_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	pollos_engorde_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	pollos_engorde_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#AVES TRASPATIO
	aves_traspatio_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	aves_traspatio_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	aves_traspatio_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#OVINOS
	ovinos_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	ovinos_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	ovinos_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#CAPRINOS
	caprinos_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	caprinos_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	caprinos_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#PECES
	peces_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	peces_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	peces_totales = models.PositiveIntegerField(blank=True,null=True,default=0)
	#BUFFALOS
	buffalos_propios = models.PositiveIntegerField(blank=True,null=True,default=0)
	buffalos_ajenos = models.PositiveIntegerField(blank=True,null=True,default=0)
	buffalos_totales = models.PositiveIntegerField(blank=True,null=True,default=0)

	def __unicode__(self):
		return self.predio.nombre_predio

class ParametroProductivo(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	#doble proposito	
	peso_vaca_produccion = models.FloatField (blank=True,null=True,default=0)
	litro_vaca_dia = models.FloatField (blank=True,null=True,default=0)
	duracion_lactancia = models.FloatField(blank=True,null=True,default=0)
	dias_abiertos = models.FloatField(blank=True,null=True,default=0)
	peso_cria_nacimiento = models.FloatField (blank=True,null=True,default=0)
	#ceba
	peso_inicial_ceba = models.FloatField (blank=True,null=True,default=0)
	edad_ceba = models.FloatField (blank=True,null=True,default=0)
	peso_final_ceba = models.FloatField (blank=True,null=True,default=0)
	ganancia_diaria_peso_ceba = models.FloatField (blank=True,null=True,default=0)
	tiempo_periodo_ceba = models.FloatField (blank=True,null=True,default=0)
	carga_animal_ceba = models.DecimalField(max_digits=4,decimal_places=2,blank=True,null=True)
	#levante
	peso_destete = models.FloatField (blank=True,null=True,default=0)
	edad_levante = models.FloatField (blank=True,null=True,default=0)
	peso_final_levante = models.FloatField (blank=True,null=True,default=0)
	ganancia_diaria_peso_levante = models.FloatField (blank=True,null=True,default=0)
	tiempo_periodo_levante = models.FloatField (blank=True,null=True,default=0)
	carga_animal_levante = models.FloatField (blank=True,null=True,default=0)

	def __unicode__(self):
		return self.predio.nombre_predio



