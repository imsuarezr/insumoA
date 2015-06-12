from django.contrib import admin
from .models import *

admin.site.register(TipoIdentificacion)
admin.site.register(EstadoCivil)
admin.site.register(RegimenSalud)
admin.site.register(Sisben)
admin.site.register(Genero)

admin.site.register(Booleanos)

admin.site.register(Cubierta)
admin.site.register(TipoConstruccion)

admin.site.register(BMR)

admin.site.register(FuenteEnergia)
admin.site.register(FuenteEnergiaPreparacionAlimentos)
admin.site.register(FormaProteccion)

admin.site.register(AguaUsoDomestico)
admin.site.register(AguaProduccion)
admin.site.register(SistemaSuccionAgua)

admin.site.register(TipoSiembra)

admin.site.register(AtractivoEcoturismo)
admin.site.register(ActividadEcoturismo)