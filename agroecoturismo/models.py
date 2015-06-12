from django.db import models
from predio.models import InfoPredioGeneral
from opciones.models import AtractivoEcoturismo, ActividadEcoturismo, Booleanos


class Agroecoturismo(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	prestacion_agrocoturismo_predio = models.ForeignKey(Booleanos,blank=True,null=True)
	atractivo = models.ManyToManyField(AtractivoEcoturismo,related_name='atractivo+',blank=True)
	actividad = models.ManyToManyField(ActividadEcoturismo,blank=True)
	observaciones = models.TextField(blank=True,null=True)

	def __unicode__(self):
		return self.predio.nombre_predio
