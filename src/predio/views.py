from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import FormView, TemplateView, UpdateView, DetailView, CreateView, ListView
from django.views.generic.edit import BaseFormView

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader

from django.shortcuts import get_object_or_404

from .forms import *
from setup.views import UpdateModelMixin, UpdateModelPredioCreadoMixin

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#ALGORITMO DE PREDIO
class InfoGeneralPredioView(TemplateView):
	template_name = 'predio/infogeneral.html'

	def dispatch(self,request,*args,**kwargs):
		predio_before = InfoPredioGeneral.objects.filter(user_id=self.request.user)
		if predio_before.count()==0:
			return HttpResponseRedirect('/informacionpredio/first/infogeneral/')
		else:
			last = InfoPredioGeneral.objects.filter(user_id=self.request.user).latest('pk')
			print(self.request.user)
			return HttpResponseRedirect('/informacionpredio/info/%s'%(last.id))
		return super(InfoGeneralPredioView,self).dispatch(request,*args,**kwargs)


class InfoGeneralPredioFirstTimeView(FormView):
	form_class = FormInfoGeneralPredio
	success_url = '/'
	template_name = 'predio/first_time/infogeneral.html'

	def form_valid(self,form):
		usuario = InfoPredioGeneral()
		usuario = form.save(commit=False)
		usuario.user = self.request.user
		usuario.save()
		return super(InfoGeneralPredioFirstTimeView,self).form_valid(form)


class PredioCreadoView(UpdateModelPredioCreadoMixin,UpdateView):
	model = InfoPredioGeneral
	form_class = FormInfoGeneralPredio
	success_url = '/'
	template_name = 'predio/infogeneral.html'

	def get_initial(self):
		return { 'departamento': '1','municipio':'1', }



#CANTIDAD DE CREDITO
class CantidadCreditoPredioView(UpdateModelMixin,UpdateView):
	model  = CantidadCreditoPredio
	form_class = FormCantidadCreditoPredio	
	success_url = '/'
	template_name = 'predio/cantidad.html'

	def post(self, request, *args, **kwargs):	
		p = 0
		x = request.POST['cantidad_credito']
		there_is_consecutive = CreditoPredio.objects.filter(predio_id=self.kwargs['predio_id']).count()
		print(there_is_consecutive)
		if there_is_consecutive==0:		
			while (p < int(x)):
				p+=1
				CreditoPredio.objects.create(predio_id=self.kwargs['predio_id'],consecutivo=p)				
		else:
			while (p < int(x)):
				p+=1
				c = CreditoPredio.objects.filter(predio_id=self.kwargs['predio_id']).latest('id')	
				l = c.consecutivo+1
				CreditoPredio.objects.create(predio_id=self.kwargs['predio_id'],consecutivo=l)			
		return super(CantidadCreditoPredioView, self).post(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(CantidadCreditoPredioView, self).get_context_data(**kwargs)
		tiene_creditos = CreditoPredio.objects.filter(predio_id=self.kwargs['predio_id'])
		if tiene_creditos.count()>=1:
			context['ir_a_creditos'] = "Ir a Creditos"		
		context['primer_credito'] = CreditoPredio.objects.filter(predio_id=self.kwargs['predio_id']).first()
		return context


#ALGORITMO DE PREDIO
class CreditoView(UpdateView):
	model = CreditoPredio
	form_class = FormCreditoPredio
	success_url = '/'
	template_name = 'predio/credito.html'


	def get_context_data(self, **kwargs):
		context = super(CreditoView, self).get_context_data(**kwargs)
		qs = CreditoPredio.objects.filter(predio_id=self.kwargs['predio_id'])
		id_list = list(qs.values_list('id', flat=True))
		position = id_list.index(int(self.kwargs['pk']))
		context['lista'] = id_list
		context['posicion'] = position
		if position == 0:
			context['no_previous'] = "Ok"
			print(context['no_previous'])
		#navigation
		siguiente = id_list[id_list.index(int(self.kwargs['pk']))]
		anterior = id_list[id_list.index(int(self.kwargs['pk']))-1]
		if siguiente:
				try:
					next_id = id_list[id_list.index(int(self.kwargs['pk'])) +1]
					obj = CreditoPredio.objects.get(predio_id=self.kwargs['predio_id'],pk=next_id)
					context['next_id'] = next_id
				except IndexError:
					pass
		if anterior:
			try:
				#prev
				prev_id = id_list[id_list.index(int(self.kwargs['pk']))-1]
				prev = CreditoPredio.objects.get(predio_id=self.kwargs['predio_id'],pk=prev_id)
				context['prev_id'] = prev_id
			except IndexError:
				pass
		return context
			
class ViviendaPredioView(UpdateModelMixin, UpdateView):
	model = ViviendaPredio
	form_class = FormViviendaPreio
	success_url = '/'
	template_name = 'predio/vivienda.html'









