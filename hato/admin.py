from django.contrib import admin
from .models import *

"""
class GanadoHembrasAdmin(admin.ModelAdmin):
	list_display = ('predio','tipo_animal','propios','ajenos','totales', )

class GanadoMachosAdmin(admin.ModelAdmin):
	list_display = ('predio','tipo_animal','propios','ajenos','totales', )
"""
admin.site.register(GanadoHembras)
admin.site.register(GanadoMachos)
admin.site.register(OtrasEspecies)

admin.site.register(ParametroProductivo)
