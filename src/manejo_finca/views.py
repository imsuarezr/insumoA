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
from opciones.models import *
from predio.models import *
from productores.models import * 
from setup.views import PredioMixin, UpdateModelMixin

class ManejoGeneralFincaView(UpdateModelMixin, UpdateView):
	model = ManejoGeneral
	form_class = FormManejoGeneral
	success_url = '/'
	template_name = 'manejo_finca/manejo_general.html'

class EnfermedadesView(UpdateModelMixin, UpdateView):
	model = Enfermedades
	form_class = FormEnfermedades
	success_url = '/'
	template_name = 'manejo_finca/enfermedades.html'




