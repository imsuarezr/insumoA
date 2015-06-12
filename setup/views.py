from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView, CreateView, FormView, ListView, TemplateView, UpdateView

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404 
from django.template import RequestContext, loader

from django.db.models import Sum, F, Q, Avg

from predio.models import *
from productores.models import *
from .forms import *
from hato.models import *
from fuentes_agua.models import *
from usos_suelo.models import *
from lacteos.models import *
from manejo_finca.models import *
from agroecoturismo.models import *

import json

from itertools import chain
	
class UpdateModelPredioCreadoMixin(object):
	def get_object(self):
		return self.model.objects.get_or_create(pk=self.kwargs['pk'],user_id=self.request.user)[0]


class UpdateModelMixin(object):
	def get_object(self):
		return self.model.objects.get_or_create(predio_id=self.kwargs['predio_id'])[0]
		
class PredioMixin(object):
	def form_valid(self,form):
		get_productor = Persona()
		get_productor = form.save(commit=False)
		get_productor.predio = InfoPredioGeneral.objects.filter(user_id=self.request.user).latest('id')
		get_productor.save()
		return super(PredioMixin,self).form_valid(form)

class LoginView(FormView):
	form_class = AuthenticationForm
	template_name = 'login.html'
	success_url = '/modulos'

	def dispatch(self,request,*args,**kwargs):
		if request.user.is_authenticated():
			return HttpResponseRedirect(self.get_success_url())
		else:
			return super(LoginView,self).dispatch(request,*args,**kwargs)

	def form_valid(self,form):
		login(self.request,form.get_user())
		return super(LoginView,self).form_valid(form)



def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')


class Modulos(TemplateView):
	template_name = 'modulos.html'


class Edit(TemplateView):
	#form_class = BuscarForm
	template_name = 'edit.html'

	def get_context_data(self, **kwargs):
		context = super(Edit, self).get_context_data(**kwargs)
		context['data'] = InfoPredioGeneral.objects.filter(user_id=self.request.user)
		#context['form'] = self.form_class
		return context

class BuscarPredio(TemplateView):
	template_name = 'edit.html'

	def post(self,request,*args,**kwargs):
		buscar_predio = request.POST['nombre_predio']
		query1 = InfoPredioGeneral.objects.filter(nombre_predio__iexact=buscar_predio)
		if query1:
			ctx  = {'predio':query1}
			return render(request,'resultados_busqueda.html',ctx)
		else:
			return render(request,'resultados_busqueda.html')

"""
class BuscarPropietario(TemplateView):
	template_name = 'edit.html'

	def post(self,request,*args,**kwargs):
		propietario = request.POST['propietario']
		query2 = Propietario.objects.filter(numero_identificacion__iexact=propietario)
		if query2:
			ctx  = {'propietario':query2}
			return render(request,'resultados_busqueda.html',ctx)
		else:
			pass
			return HttpResponse("aja")
			#return render(request,'resultados_busqueda.html')
"""





class RemoveView(DetailView):
	model = InfoPredioGeneral
	template_name = 'reportes.html'

	def post(self,request,*args,**kwargs):
		pass_p = request.POST['predio']
		p = InfoPredioGeneral.objects.get(pk=int(pass_p))
		p.delete()
		data = {}
 	  	data['success'] = "Predio eliminado"
 	  	return HttpResponse(json.dumps(data), content_type='application/json')

		
class ListaReportesView(ListView):
	model = InfoPredioGeneral
	template_name = 'reportes.html'


class ReportesView(DetailView):
	model = InfoPredioGeneral
	template_name = 'reporteprueba.html'

	def get_context_data(self, **kwargs):
		context = super(ReportesView, self).get_context_data(**kwargs)
		#predio
		context['predio'] = InfoPredioGeneral.objects.get(pk=self.kwargs['pk'])
		#creditos
		context['creditos'] = CreditoPredio.objects.filter(predio_id=self.kwargs['pk'])
		#propietario administrador y encargados
		if Propietario.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			Propietario.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['propietario'] = Propietario.objects.get(predio_id=self.kwargs['pk'])

		if Administrador.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			Administrador.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['administrador'] = Administrador.objects.get(predio_id=self.kwargs['pk'])

		if Encargado.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			Encargado.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['encargado'] = Encargado.objects.get(predio_id=self.kwargs['pk'])
		
		#vivienda
		if ViviendaPredio.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			ViviendaPredio.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['vivienda'] = ViviendaPredio.objects.filter(predio_id=self.kwargs['pk'])
		
		context['creditos'] = CreditoPredio.objects.filter(predio_id=self.kwargs['pk'])

		#FUENTES DE AGUA
		#nacimientos de agua
		if NacimientosAgua.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			NacimientosAgua.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['nacimientosagua'] = NacimientosAgua.objects.get(predio_id=self.kwargs['pk'])	
	
		#usos de agua
		if ViviendaUsos.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			ViviendaUsos.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['usosagua'] = ViviendaUsos.objects.filter(predio_id=self.kwargs['pk'])
		
		
		#USOS SUELOS
		#actividades pecuarias
		if Pastoreo.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			Pastoreo.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['pastoreo'] = Pastoreo.objects.get(predio_id=self.kwargs['pk'])
		#bancos forraje
		if BancosForraje.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			BancosForraje.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['bancosforraje'] = BancosForraje.objects.get(predio_id=self.kwargs['pk']) 
		#actividades agricolas y forestales
		if CultivoAgricolasYForestales.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			CultivoAgricolasYForestales.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['agricolasyforestales'] = CultivoAgricolasYForestales.objects.get(predio_id=self.kwargs['pk']) 	
		
		#HATO
		#consultas hembras
		if GanadoHembras.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			GanadoHembras.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['ganadohembras'] = GanadoHembras.objects.get(predio_id=self.kwargs['pk'])
		
		#consultas machos
		if GanadoMachos.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			GanadoMachos.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['ganadomachos'] = GanadoMachos.objects.get(predio_id=self.kwargs['pk'])
		
		#otras especies
		if OtrasEspecies.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			OtrasEspecies.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['otrasespecies'] = OtrasEspecies.objects.get(predio_id=self.kwargs['pk'])
		
		#parametros productivos
		if ParametroProductivo.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			ParametroProductivo.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['parametrosproductivos'] = ParametroProductivo.objects.get(predio_id=self.kwargs['pk'])	
		
		#LACTEOS
		#produccion leche
		if ProduccionLeche.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			ProduccionLeche.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['leche'] = ProduccionLeche.objects.get(predio_id=self.kwargs['pk'])

		#suplementos
		if Suplementos.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			Suplementos.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['suplementos'] = Suplementos.objects.get(predio_id=self.kwargs['pk'])

		#insumos
		if Insumos.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			Insumos.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['insumos'] = Insumos.objects.get(predio_id=self.kwargs['pk'])

		#MANEJO GENERAL DE LA FINCA
		#manejo general
		if ManejoGeneral.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			ManejoGeneral.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['finca'] = ManejoGeneral.objects.filter(predio_id=self.kwargs['pk'])

		#enfermedades frecuentes
		if Enfermedades.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			Enfermedades.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['enfermedades'] = Enfermedades.objects.filter(predio_id=self.kwargs['pk'])

		#AGROECOTURISMO
		if Agroecoturismo.objects.filter(predio_id=self.kwargs['pk']).count()==0:
			Agroecoturismo.objects.create(predio_id=self.kwargs['pk'])
		else:
			context['agroecoturismo'] = Agroecoturismo.objects.filter(predio_id=self.kwargs['pk'])
		
		#CONSULTA DE SUMAS TOTALES

		#habitantes 
		suma_habitantes =  Habitantes.objects.filter(predio_id=self.kwargs['pk'])
		for habitantes in suma_habitantes:
			context['suma_habitantes'] = int(habitantes.total_ninos)+int(habitantes.total_adultos)+int(habitantes.total_adultos_mayores)

		#hato
		suma_machos = GanadoMachos.objects.filter(predio_id=self.kwargs['pk'])
		for m in suma_machos:
			context['suma_machos']= int(m.toros_totales)+int(m.machos_mayores_3_anios_totales)+int(m.machos_2_a_3_anios_totales)+int(m.machos_1_a_2_anios_totales)+int(m.machos_menores_1_anio_totales)+int(m.bueyes_totales)
		
		suma_hembras = GanadoHembras.objects.filter(predio_id=self.kwargs['pk'])
		for h in suma_hembras:
			context['suma_hembras']= int(h.vacas_paridas_totales)+int(h.vacas_horras_totales)+int(h.vacas_23_totales)+int(h.vacas_12_totales)+int(h.vacas_menores_totales)+int(h.vacas_descarte_totales)
		
		otras_especias = OtrasEspecies.objects.filter(predio_id=self.kwargs['pk'])
		for o in otras_especias:
			context['suma_otras_especias']= int(o.caballares_totales)+int(o.mulares_totales)+int(o.cochino_sabanero_totales)+int(o.cerdos_confinamiento_totales)+int(o.gallina_encasetada_totales)+int(o.pollos_engorde_totales)+int(o.aves_traspatio_totales)+int(o.ovinos_totales)+int(o.caprinos_totales)+int(o.peces_totales)+int(o.buffalos_totales)

		#cultivos agricolas y forestales
		pecuarios = Pastoreo.objects.filter(predio_id=self.kwargs['pk'])
		bancos_forraje = BancosForraje.objects.filter(predio_id=self.kwargs['pk'])
		for p in pecuarios:
			suma_pecuarios = int(p.pasturas_nativas_sin_arboles)+int(p.pasturas_introducidas_sin_arboles)+int(p.sistema_silvopastoril_intensivo)+int(p.sistema_silvopastoril_intensivo_con_maderables)+int(p.arboles_dispersos_en_potreros)+int(p.franjas_dobles_arboles_en_potreros)+int(p.cercas_vivas)
		for b in bancos_forraje:
			suma_bancos_forraje= int(b.bancos_energia)+int(b.bancos_proteina)+int(b.bancos_mixtos)		
		context['suma_pasturas_mas_forraje'] = suma_pecuarios+suma_bancos_forraje

		sumas_cultivos_agricolas = CultivoAgricolasYForestales.objects.filter(predio_id=self.kwargs['pk'])
		for a in sumas_cultivos_agricolas:
			context['suma_agricolas'] = int(a.maiz)+int(a.platano)+int(a.cafe)+int(a.maiz_con_platano)+int(a.cafe_con_platano)+int(a.platano_con_cacao)
			context['suma_forestales'] = int(a.eucalipto)+int(a.pino)+int(a.teca)+int(a.teca_mas_melina)+int(a.pardillo_mas_tolua)

		#lacteos
		suplementos = Suplementos.objects.filter(predio_id=self.kwargs['pk'])
		for s in suplementos:
			context['suma_suplementos'] = int(s.sal_blanca_total)+int(s.sal_mineralizada_total)+int(s.premezcla_mineral_total)+int(s.azufre_total)+int(s.concentrado_total)+int(s.melaza_total)+int(s.heno_total)+int(s.ensilaje_total)

		insumos = Insumos.objects.filter(predio_id=self.kwargs['pk'])
		for i in insumos:
			context['suma_insumos'] = int(i.parasitos_externos_total)+int(i.alambre_pua_total)+int(i.alambre_electrica_total)+int(i.gallinaza_compostada_total)+int(i.servicios_veterinarios_total)+int(i.postes_total)+int(i.medicamentos_total)+int(i.herbicidas_total)+int(i.fertilizantes_quimicos_total)+int(i.fertilizantes_organicos_total)+int(i.antiparasitarios_total)++int(i.herramientas_accesorios_total)

		return context

class ReportePrueba(TemplateView):
	template_name = 'reporte-1-falso.html'

#comparacion de predios

class ComparacionFormView(ListView):
	model = InfoPredioGeneral
	template_name = 'comparar.html'

class Comparacion(ListView):
	model = InfoPredioGeneral
	template_name = 'comparacion.html'

	def post(self,request,*args,**kwargs):
		predios = request.POST.getlist('comparacion')
		comparativos = (predios)
		predio = InfoPredioGeneral.objects.filter(pk__in=(comparativos))
		hembras = GanadoHembras.objects.filter(predio_id__in=(comparativos))
		machos = GanadoMachos.objects.filter(predio_id__in=(comparativos))
		otras_especies = OtrasEspecies.objects.filter(predio_id__in=(comparativos))
		if predio:
			
			lista_hembras=[]
			for hembra in hembras:
				comparacion_hembras = hembra
				t = lista_hembras.append(dict([(hembra,comparacion_hembras)]))
			
			lista_machos = []
			for macho in machos:
				comparacion_machos = macho
				x =  lista_machos.append(dict([(macho,comparacion_machos)]))
			
			lista_otras_especies = []
			for otra_especie in otras_especies:
				comparacion_otras_especies = otra_especie
				p = lista_otras_especies.append(dict([(otra_especie,comparacion_otras_especies)]))
			ctx = {'hembras':lista_hembras,'machos':lista_machos,'otras_especies':lista_otras_especies}
			print(ctx)
			return render(request,'comparacion.html',ctx)




	
"""
		if comparativos:
			ctx  = {'comparativo':comparativos}
			return render(request,'comparacion.html',ctx)
		else:
			return render(request,'comparacion.html')
"""		



