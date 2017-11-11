from django import forms
from django.db import models
from django.forms import formset_factory
from django.utils import timezone
import re
from django.forms import BaseModelFormSet
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from .models import Corso, Iscrizione



class CreaCorsi(forms.ModelForm):
    class Meta:
        model = Corso
        fields = ['titolo', 'studenti_referenti', 'classi_autori', 'descrizione','aule', 'progressivo','f1','f2','f3','f4','f5','f6','f7','f8' ]




class IscrizioneForm(forms.ModelForm):
    class Meta:
        model = Iscrizione
        fields = ['corso1', 'corso2', 'corso3', 'corso4', 'corso5', 'corso6', 'corso7', 'corso8']
        

class Mail(forms.Form):
    testo=forms.CharField(widget=forms.TextInput(attrs={'form-control': 'form-control'}))
    mail= forms.EmailField(widget=forms.TextInput(attrs={'form-control': 'form-control'}))
