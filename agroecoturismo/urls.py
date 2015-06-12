from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('agroecoturismo.views',
	url(r'^agro/agroecoturismo/(?P<predio_id>\d+)/$', AgroecoturismoView.as_view(),name='agroecoturismo'),
	) 




