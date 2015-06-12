from django.conf.urls import patterns,url
from .views import *
from .models import *
from .forms import *

urlpatterns = patterns('predio.views',
	
	url(r'^informacionpredio/infogeneral/.*$', InfoGeneralPredioView.as_view(),name='prediogeneral'),
	url(r'^informacionpredio/first/infogeneral/.*$', InfoGeneralPredioFirstTimeView.as_view(),name='prediogeneralfirstime'),
	url(r'^informacionpredio/info/(?P<pk>[-_\w]+)/$', PredioCreadoView.as_view(),name='prediocreado'),
	
	url(r'^informacionpredio/cantidad-creditos/(?P<predio_id>[-_\w]+)/$', CantidadCreditoPredioView.as_view(),name='cantidad'),

	#url(r'^informacionpredio/creditos/(?P<predio_id>[-_\w]+)/(?P<pk>[-_\w]+)/$', CreditoIndividualPredioView.as_view(),name='creditos'),
	
	url(r'^informacionpredio/creditos/(?P<predio_id>[-_\w]+)/(?P<pk>[-_\w]+)/$', CreditoView.as_view(),name='creditos'),
	


	#url(r'^informacionpredio/guardar-credito/(?P<predio_id>[-_\w]+)/(?P<pk>[-_\w]+)/$', FormCreditoView.as_view(),name='creditos'),
	url(r'^informacionpredio/vivienda/(?P<predio_id>[-_\w]+)/$', ViviendaPredioView.as_view(),name='vivienda'),

	
	
	) 




