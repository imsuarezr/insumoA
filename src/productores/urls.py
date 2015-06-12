from django.conf.urls import patterns,url
from .views import *
urlpatterns = patterns('productores.views',
	
	#PAE
	url(r'^pae/propietario/(?P<predio_id>\d+)/$', PAEPropietarioView.as_view(),name='propietario'),
	url(r'^pae/administrador/(?P<predio_id>\d+)/$', PAEAdministradorView.as_view(),name='administrador'),
	url(r'^pae/encargado/(?P<predio_id>\d+)/$', PAEEncargadoView.as_view(),name='encargado'),
	#PE
	url(r'^pe/propietario/(?P<predio_id>\d+)/$', PropietarioAndAdministratorView.as_view(),name='propietario'),
	url(r'^pe/encargado/(?P<predio_id>\d+)/$', PEEncargadoView.as_view(),name='propietario'),
	#E
	url(r'^e/propietario/(?P<predio_id>\d+)/$', PropietarioAdminEncargadoView.as_view(),name='propietario'),
	url(r'^productor/habitantes/(?P<predio_id>\d+)/$', HabitantesView.as_view(),name='habitantes'),
	

	)
	

		
	





