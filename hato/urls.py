from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('hato.views',
	url(r'^hato/hembras/(?P<predio_id>[-_\w]+)/$', InventarioHembrasView.as_view(),name='hembras'),
	url(r'^hato/machos/(?P<predio_id>[-_\w]+)/$', InventarioMachosView.as_view(),name='machos'),
	url(r'^hato/otras-especies/(?P<predio_id>[-_\w]+)/$', OtrasEspeciesView.as_view(),name='otras_especies'),
	url(r'^hato/doble-proposito/(?P<predio_id>[-_\w]+)/$', DoblePropositoView.as_view(),name='doble_proposito'),


	) 




