from django.db import models
from predio.models import InfoPredioGeneral
from opciones.models import Booleanos


class EnfoqueDiferencial(models.Model):
	predio = models.ForeignKey(InfoPredioGeneral)
	es_victima = models.ForeignKey(Booleanos,related_name='es victima+',blank=True,null=True)
	observaciones = models.TextField(blank=True,null=True)

	def __unicode__(self):
		return self.predio.nombre_predio