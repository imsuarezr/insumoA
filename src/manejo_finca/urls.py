from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('manejo_finca.views',
	url(r'^manejo-finca/manejo-general/(?P<predio_id>\d+)/.*$', ManejoGeneralFincaView.as_view(),name='manejogeneral'),
	url(r'^manejo-finca/enfermedades/(?P<predio_id>\d+)/.*$', EnfermedadesView.as_view(),name='enfermedadas'),
	
	) 




