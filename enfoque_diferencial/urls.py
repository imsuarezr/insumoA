from django.conf.urls import patterns,url
from .views import *

urlpatterns = patterns('enfoque_diferencial.views',
	url(r'^enf/enfoque_diferencial/(?P<predio_id>\d+)/$', EnfoqueDiferencialView.as_view(),name='enfoque_diferencial'),
	) 




