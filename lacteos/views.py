from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import FormView, TemplateView, CreateView, UpdateView, ListView
from django.views.generic.edit import BaseFormView

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader

from .forms import *
from .models import *
from predio.models import *
from setup.views import PredioMixin, UpdateModelMixin



class ProduccionLecheView(UpdateModelMixin,UpdateView):
	model = ProduccionLeche
	form_class = FormProduccionLeche
	success_url = '/'
	template_name = 'lacteos/produccion_leche.html'

class SuplementosView(UpdateModelMixin,UpdateView):
	model = Suplementos
	form_class = FormSuplementos
	success_url = '/'
	template_name = 'lacteos/suplementos.html'


class InsumosView(UpdateModelMixin,UpdateView):
	model = Insumos
	form_class = FormInsumos
	success_url = '/'
	template_name = 'lacteos/insumos.html'



