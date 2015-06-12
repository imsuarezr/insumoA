from django.contrib import admin
from .models import *


class CreditoPredioAdmin(admin.ModelAdmin):
	list_display = ('pk','predio','consecutivo')

admin.site.register(InfoPredioGeneral)
admin.site.register(DocumentoAcreditacion)

admin.site.register(CreditoPredio,CreditoPredioAdmin)
admin.site.register(CantidadCreditoPredio)
 

admin.site.register(ViviendaPredio)
