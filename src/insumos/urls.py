from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'insumos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('setup.urls')),
    url(r'^',include('productores.urls')),
    url(r'^',include('predio.urls')),
    url(r'^',include('fuentes_agua.urls')),
    url(r'^',include('usos_suelo.urls')),
    url(r'^',include('manejo_finca.urls')),
    url(r'^',include('hato.urls')),
    url(r'^',include('lacteos.urls')),
    url(r'^',include('agroecoturismo.urls')),
    url(r'^',include('enfoque_diferencial.urls')),

]
urlpatterns += staticfiles_urlpatterns()


