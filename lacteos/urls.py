from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('lacteos.views',
	url(r'^lacteos/produccion-leche/(?P<predio_id>\d+)/$', ProduccionLecheView.as_view(),name='produccionleche'),
	url(r'^lacteos/suplementos/(?P<predio_id>\d+)/$', SuplementosView.as_view(),name='suplementos'),
	url(r'^lacteos/insumos/(?P<predio_id>\d+)/$', InsumosView.as_view(),name='insumos'),

	
	) 




