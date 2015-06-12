from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import FormView, TemplateView, CreateView, UpdateView
from django.views.generic.edit import BaseFormView

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader

from .forms import *
from .models import *
from predio.models import *
from setup.views import PredioMixin, UpdateModelMixin

class PastoreoView(UpdateModelMixin, UpdateView):
	model = Pastoreo
	form_class = FormPastoreo
	success_url = '/'
	template_name = 'usos_suelo/pastoreo.html'

class BancosForrajeView(UpdateModelMixin, UpdateView):
	model = BancosForraje
	form_class = FormBancosForraje
	success_url = '/'
	template_name = 'usos_suelo/bancosforraje.html'

class CultivosAgricolasView(UpdateModelMixin, UpdateView):
	model = CultivoAgricolasYForestales
	form_class = FormCultivosAgricolas
	success_url = '/'
	template_name = 'usos_suelo/cultivos_agricolas_forestales.html'



