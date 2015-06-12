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
from opciones.models import *
from setup.views import UpdateModelMixin, PredioMixin

from django.shortcuts import get_object_or_404


#PAE
class PAEPropietarioView(UpdateModelMixin,UpdateView):
	model = Propietario
	form_class = FormPropietario
	success_url = '/'
	template_name = 'productores/PAE/propietario.html'

	def form_valid(self,form):
		propietario = Propietario()
		propietario = form.save(commit=False)
		return super(PAEPropietarioView,self).form_valid(form)

class PAEAdministradorView(UpdateModelMixin,UpdateView):
	model = Administrador
	form_class = FormAdministrador
	success_url = '/'
	template_name = 'productores/PAE/administrador.html'

	def form_valid(self,form):
		administrador = Administrador()
		administrador = form.save(commit=False)
		return super(PAEAdministradorView,self).form_valid(form)

class PAEEncargadoView(UpdateModelMixin,UpdateView):
	model = Encargado
	form_class = FormEncargado
	success_url = '/'
	template_name = 'productores/PAE/encargado.html'

	def form_valid(self,form):
		encargado = Encargado()
		encargado = form.save(commit=False)
		return super(PAEEncargadoView,self).form_valid(form)

#PE
class PropietarioAndAdministratorView(UpdateModelMixin,UpdateView):
	model = Propietario
	form_class = FormPropietario
	success_url = '/'
	template_name = 'productores/PE/propietario.html'

	def form_valid(self, form):
		form.prop_admin(predio_id=self.kwargs['predio_id'])
		return super(PropietarioAndAdministratorView, self).form_valid(form)


class PEEncargadoView(UpdateModelMixin,UpdateView):
	model = Encargado
	form_class = FormEncargado
	success_url = '/'
	template_name = 'productores/PE/encargado.html'

	def form_valid(self,form):
		encargado = Encargado()
		encargado = form.save(commit=False)
		return super(PEEncargadoView,self).form_valid(form)

#E
class PropietarioAdminEncargadoView(UpdateModelMixin,UpdateView):
	model = Encargado
	form_class = FormEncargado
	success_url = '/'
	template_name = 'productores/E/propietario.html'

	def form_valid(self, form):
		form.prop_admin_enc(predio_id=self.kwargs['predio_id'])
		return super(PropietarioAdminEncargadoView, self).form_valid(form)


class HabitantesView(UpdateModelMixin,UpdateView):
	model = Habitantes
	form_class = FormHabitantes
	success_url = '/'
	template_name = 'productores/habitantes.html'

