from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('fuentes_agua.views',
	url(r'^fuentesagua/nacimientos/(?P<predio_id>[-_\w]+)/$', NacimientosAguaView.as_view(),name='nacimientos'),
	url(r'^fuentesagua/usos/(?P<predio_id>[-_\w]+)/$', UsosAguaView.as_view(),name='usos'),

	) 




