from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import FormView, TemplateView, UpdateView, CreateView
from django.views.generic.edit import BaseFormView

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext, loader

from .forms import *
from opciones.models import *
from predio.models import *
from productores.models import * 
from .models import *
from setup.views import PredioMixin, UpdateModelMixin


class InventarioHembrasView(UpdateModelMixin,UpdateView):
	model = GanadoHembras
	form_class = FormInventarioHembras
	success_url = '/'
	template_name = 'hato/hembras.html'


class InventarioMachosView(UpdateModelMixin,UpdateView):
	model = GanadoMachos
	form_class = FormInventarioMachos
	success_url = '/'
	template_name = 'hato/machos.html'


class OtrasEspeciesView(UpdateModelMixin,UpdateView):
	model = OtrasEspecies
	form_class = FormOtrasEspecies
	success_url = '/'
	template_name = 'hato/otras_especies.html'

class DoblePropositoView(UpdateModelMixin,UpdateView):
	model = ParametroProductivo
	form_class = FormDobleProposito
	success_url = '/'
	template_name = 'hato/doble_proposito.html'


