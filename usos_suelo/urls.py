from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('usos_suelo.views',
	url(r'^usossuelo/pastoreo/(?P<predio_id>\d+)/$', PastoreoView.as_view(),name='pastoreo'),
	url(r'^usossuelo/bancos-forraje/(?P<predio_id>\d+)/$', BancosForrajeView.as_view(),name='bancosforraje'),
	url(r'^usossuelo/cultivos-agricolas/(?P<predio_id>\d+)/$', CultivosAgricolasView.as_view(),name='cultivos'),
	) 




