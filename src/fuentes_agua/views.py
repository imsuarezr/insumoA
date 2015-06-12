from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import FormView, TemplateView, UpdateView, CreateView
from django.views.generic.edit import BaseFormView

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader

from .forms import *
from setup.views import PredioMixin, UpdateModelMixin

class NacimientosAguaView(UpdateModelMixin, UpdateView):
	model = NacimientosAgua
	form_class = FormNacimientosAgua
	success_url = '/'
	template_name = 'fuentes_agua/nacimientos_agua.html'

class UsosAguaView(UpdateModelMixin, UpdateView):
	model = ViviendaUsos
	form_class = FormUsosAgua
	success_url = '/'
	template_name = 'fuentes_agua/usos_agua.html'


