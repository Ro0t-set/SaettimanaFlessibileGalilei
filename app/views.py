# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from .models import Corso, Iscrizione
from django.shortcuts import render, get_object_or_404
from .forms import CreaCorsi, IscrizioneForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
import operator
from django.db.models import Q
from django.forms import formset_factory
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models import Count
from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator

@csrf_protect


def crea(request):
#    corsi= Corso.objects.all()
#    print (corsi.count())
#    print ('funge')
#    if corsi.count() > 4:
#        print('errore')
#    else:
#        print('successo')



    if request.method == "POST":

        form = CreaCorsi(request.POST)

        if form.is_valid():

            corso = form.save(commit=False)
            corso.author = request.user
            corso.published_date = timezone.now()
            corso.save()
            return redirect('home')

    else:
        form = CreaCorsi()

    return render(request, 'corsi/crea.html', {'form' : form })


def home (request):
     corsi = Corso.objects.all()

     return render(request, 'corsi/home.html', {'corsi': corsi})



@login_required
def privata(request):

    iscrizioni= Iscrizione.objects.filter(user=request.user)


    return render(request, 'corsi/privata.html', {'iscrizioni':iscrizioni})

@login_required

def edit_iscrizioni(request):
    corsi = request.GET.get("a")
    if corsi:
        corsi = Corso.objects.filter(id= corsi)

    if request == "POST":
        form= IscrizioneForm(request.POST)
        if form.is_valid():
            iscrizioni = form.save(commit= False)
            iscrizioni.author= request.user
            iscrizioni.save()
            return redirect('privata')
    else:
        form= IscrizioneForm()
    return render(request, 'corsi/edit.html', {'form':form, 'corsi':corsi})


# @login_required
# def iscrizioni(request, id):
#
#
#     corsi = request.GET.get("a")
#     if corsi:
#         corsi = Corso.objects.filter(id= corsi)
#         corsi = get_object_or_404(iscrizioni, id=id)
#
#
#
#         if request.method == 'POST':
#             form = IscrizioneForm(request.POST, corsi=corsi )
#             if form.is_valid():
#                 iscrizione = form.save(commit=False)
#                 iscrizione.user = request.user
#                 iscrizione.published_date = timezone.now()
#                 iscrizione.save()
#                 return redirect('home')
#
#
#         else:
#             form = IscrizioneForm()
#     return render(request, 'corsi/iscrizioni.html', {'corsi' : corsi, 'form':form })

@login_required
def filtro_fasce(request):
    corsi=request.GET.get("f")
    if corsi == 'f1':
        corsi = Corso.objects.filter(lunedi1=True)
    if corsi == 'f2':
        corsi = Corso.objects.filter(lunedi2=True)
    if corsi == 'f3':
        corsi = Corso.objects.filter(lunedi3=True)
    if corsi == 'f4':
        corsi = Corso.objects.filter(martedi1=True)
    if corsi == 'f5':
        corsi = Corso.objects.filter(martedi2=True)
    if corsi == 'f6':
        corsi = Corso.objects.filter(martedi3=True)
    if corsi == 'f7':
        corsi = Corso.objects.filter(mercoledi1=True)
    if corsi == 'f8':
        corsi = Corso.objects.filter(mercoledi2=True)
    if corsi == 'f9':
        corsi = Corso.objects.filter(mercoledi3=True)
    return render(request, 'corsi/filtro_fasce.html', {'corsi' : corsi})
