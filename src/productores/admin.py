from django.contrib import admin
from .models import *


class AdministradorAdmin(admin.ModelAdmin):
	list_display = ('pk','predio', 'primer_nombre', )


admin.site.register(Propietario)
admin.site.register(Administrador,AdministradorAdmin)
admin.site.register(Encargado)

admin.site.register(Habitantes)




