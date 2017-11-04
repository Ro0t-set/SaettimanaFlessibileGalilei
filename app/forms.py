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
        fields = ['titolo', 'autori', 'descrizione','classi_autori','aule', 'progressivo','lunedi1','lunedi2','lunedi3','martedi1','martedi2','martedi3','mercoledi1','mercoledi2','mercoledi3' ]




class IscrizioneForm(forms.ModelForm):
    class Meta:
        model = Iscrizione
        fields = []


class Mail(forms.Form):
    testo=forms.CharField(label='testo', max_length="1000")
    mail= forms.EmailField(label='mail', max_length="100")
