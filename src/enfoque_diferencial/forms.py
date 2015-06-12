from django import forms
from django.forms import ModelForm
from .models import *

class FormEnfoqueDiferencial(ModelForm):
	class Meta():
		model = EnfoqueDiferencial
		exclude = ("predio",)

class EnfoqueDiferencialEditForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(EnfoqueDiferencialEditForm, self).__init__(*args, **kwargs)
	class Meta:
		model = EnfoqueDiferencial
		exclude = ('predio',)
