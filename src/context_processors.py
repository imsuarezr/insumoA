import django
from predio.models import *
from django.views.generic import DetailView, CreateView, FormView, ListView, TemplateView, UpdateView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404 
import urlparse
from os.path import splitext, basename


def hola(request):
	if request.get_full_path().split('/')[1]=="" or request.get_full_path().split('/')[1]=="edit" or request.get_full_path().split('/')[1]=="admin" or request.get_full_path().split('/')[1]=="reportes" or request.get_full_path().split('/')[2]=="first" or request.get_full_path().split('/')[1]=="modulos" or request.get_full_path().split('/')[1]=="reporte" or request.get_full_path().split('/')[1]=="buscar" or request.get_full_path().split('/')[1]=="eliminar" or request.get_full_path().split('/')[1]=="comparacion" or request.get_full_path().split('/')[1]=="comparar-predios":
		pass
		context = {'y':'y'}
		return context
	else:
		pass
		l = request.get_full_path().split('/')
		if (len(l))>=4:
			#print(request.get_full_path().split('/')[3])
			o = request.get_full_path().split('/')[3]
			p = InfoPredioGeneral.objects.filter(id=o)
			context = {'p':p}
			return context


def my_processor(request):
	#x = InfoPredioGeneral.objects.filter(user_id=request.user)
	x = InfoPredioGeneral.objects.all()
	contador = x.count()
	if contador ==0:
		y = "hola"
		context = {'y':y}
		return context
		if request.get_full_path()=="/":
			y = "hola"
			context = {'y':y}
			return context
		else:
			y = "hola"
			context = {'y':y}
			return context
			
"""
			if request.get_full_path().split('/')[1]=="admin" or request.get_full_path().split('/')[2]=="first" or request.get_full_path().split('/')[1]=="reporte":
				#print (request.get_full_path().split('/')[1])
				print(request.get_full_path())
				pass
				context = {'y':'y'}
				return context
			else:
				l = request.get_full_path().split('/')
				if (len(l))>=4:
					print(request.get_full_path().split('/')[3])
					o = request.get_full_path().split('/')[3]
					p = InfoPredioGeneral.objects.filter(id=o)
					context = {'p':p}
					return context
				else:
					pass
					context = {'p':'p'}
				return context
"""			

"""
			if request.get_full_path().split('/')[2]=="first":
				print (request.get_full_path().split('/')[1])
				pass
				context = {'y':'y'}
				return context
			else:
				pass
				context = {'y':'y'}
				return context	
"""		













