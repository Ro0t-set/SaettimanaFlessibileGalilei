# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.utils import timezone
from .models import Corso, Iscrizione
from django.shortcuts import get_object_or_404, render
from .forms import CreaCorsi, IscrizioneForm, Mail, CercaCorsi
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
#from __future__ import unicode_literals
import datetime
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
from django.template.loader import render_to_string
from django.http import Http404
from django.contrib import messages
@csrf_protect

def errore(request):
    return render(request, 'corsi/errore.html')

def successo(request):
    return render(request, 'corsi/successo.html')

def errorefasciapiena(request):
    return render(request, 'corsi/errore_fasciapiena.html')

def disp_classi(request):
    return render(request, 'corsi/disp_classi.html')

def disp_classi_arte(request):
    return render(request, 'corsi/disp_classi_arte.html')

def disp_classi_informatica(request):
    return render(request, 'corsi/disp_classi_informatica.html')

def disp_classi_magna(request):
    return render(request, 'corsi/disp_classi_magna.html')

def disp_classi_palestra(request):
    return render(request, 'corsi/disp_classi_palestra.html')

@login_required(login_url='/login/')
def crea(request):


    if request.method == "POST":

        form = CreaCorsi(request.POST)

        if form.is_valid():

            corso = form.save(commit=False)
            corso.author = request.user
            corso.published_date = timezone.now()


            subject, from_email, to = 'corsi', 'settimanaflessibile@gmail.com', 'settimanaflessibile@gmail.com'
            text_content = '456'
            html_content =  ( str(form) )





            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            corso.save()
            msg.send()

            return redirect('successo')

    else:
        form = CreaCorsi()

    return render(request, 'corsi/crea.html', {'form' : form })


def home (request):
     corsi = Corso.objects.all()

     return render(request, 'corsi/home.html', {'corsi': corsi})

@login_required(login_url='/login/')
def tabelle (request):
     cerca = request.GET.get("q")
     form = CercaCorsi(request.GET)
     corsi = Corso.objects.all()
     contatore1= Corso.objects.filter(f1=True)
     contatore2= Corso.objects.filter(f2=True)
     contatore3= Corso.objects.filter(f3=True)
     contatore4= Corso.objects.filter(f4=True)
     contatore5= Corso.objects.filter(f5=True)
     contatore6= Corso.objects.filter(f6=True)
     contatore7= Corso.objects.filter(f7=True)
     contatore8= Corso.objects.filter(f8=True)
     contatore9= Corso.objects.filter(f9=True)

     contatore=[contatore1.count(),contatore2.count(),contatore3.count(),contatore4.count(),contatore5.count(),contatore6.count(),contatore7.count(),contatore8.count(),contatore9.count()]
     if form.is_valid():
         corsi = Corso.objects.filter(Q(titolo__icontains=cerca)|
         Q(studenti_referenti__icontains=cerca)|
         Q(aule__aule__exact=cerca))




     return render(request, 'corsi/tabelle.html', {'corsi': corsi,  'form':form , 'contatore':contatore})



@login_required(login_url='/login/')
def privata(request):

    iscrizioni= Iscrizione.objects.filter(user=request.user)
    return render(request, 'corsi/privata.html', {'iscrizioni':iscrizioni})

@login_required(login_url='/login/')
def appelli(request, corso_id):
    corsi = Corso.objects.filter( pk=corso_id)
    fasca = Corso.objects.get( pk=corso_id)

    appello=[
    list(Iscrizione.objects.filter(corso1_id=fasca).values_list('user__username', flat=True)),
    list(Iscrizione.objects.filter(corso2_id=fasca).values_list('user__username', flat=True)),
    list(Iscrizione.objects.filter(corso3_id=fasca).values_list('user__username', flat=True)),
    list(Iscrizione.objects.filter(corso4_id=fasca).values_list('user__username', flat=True)),
    list(Iscrizione.objects.filter(corso5_id=fasca).values_list('user__username', flat=True)),
    list(Iscrizione.objects.filter(corso6_id=fasca).values_list('user__username', flat=True)),
    list(Iscrizione.objects.filter(corso7_id=fasca).values_list('user__username', flat=True)),
    list(Iscrizione.objects.filter(corso8_id=fasca).values_list('user__username', flat=True)),
    list(Iscrizione.objects.filter(corso9_id=fasca).values_list('user__username', flat=True)),
    ]



    return render(request, 'corsi/appello.html', {'appello':appello})


@login_required(login_url='/login/')
def edit_iscrizioni(request, corso_id):
    corsi = Corso.objects.filter( pk=corso_id)
    fasca = Corso.objects.get( pk=corso_id)
    tabella= Iscrizione.objects.filter(user=request.user)
    iscrizione=get_object_or_404(Iscrizione, pk=tabella)
    classe_max= fasca.aule.max_iscritti
    singoli=request.GET.get("f")


    if fasca.progressivo:
        tabellagrafica=[fasca.f1, fasca.f2, fasca.f3, fasca.f4, fasca.f5, fasca.f6, fasca.f7, fasca.f8, fasca.f9]
    else:
        tabellagrafica= singoli


    contatore1= Iscrizione.objects.filter(corso1_id=fasca)
    contatore2= Iscrizione.objects.filter(corso2_id=fasca)
    contatore3= Iscrizione.objects.filter(corso3_id=fasca)
    contatore4= Iscrizione.objects.filter(corso4_id=fasca)
    contatore5= Iscrizione.objects.filter(corso5_id=fasca)
    contatore6= Iscrizione.objects.filter(corso6_id=fasca)
    contatore7= Iscrizione.objects.filter(corso7_id=fasca)
    contatore8= Iscrizione.objects.filter(corso8_id=fasca)
    contatore9= Iscrizione.objects.filter(corso9_id=fasca)


    if singoli=='f1':
        contatore=contatore1.count()
    if singoli=='f2':
        contatore=contatore2.count()
    if singoli=='f3':
        contatore=contatore3.count()
    if singoli=='f4':
        contatore=contatore4.count()
    if singoli=='f5':
        contatore=contatore5.count()
    if singoli=='f6':
        contatore=contatore6.count()
    if singoli=='f7':
        contatore=contatore7.count()
    if singoli=='f8':
        contatore=contatore8.count()
    if singoli=='f9':
        contatore=contatore9.count()



    if contatore>=classe_max:
        messages.error(request, 'Corso pieno!')
        return redirect('/filtro_fasce/?f='+singoli)
    else:


        if request.method == "POST":
            form = IscrizioneForm(request.POST, instance= iscrizione)


            if form.is_valid():
                iscrizione = form.save(commit=False)
                iscrizione.user = request.user
                iscrizione.published_date = timezone.now()
                if fasca.progressivo:

                    if contatore<classe_max:

                        if fasca.f1 and iscrizione.corso1_id != None:
                            return redirect('errorefasciapiena')

                        if fasca.f2 and iscrizione.corso2_id != None:
                            return redirect('errorefasciapiena')

                        if fasca.f3 and iscrizione.corso3_id != None:
                            return redirect('errorefasciapiena')

                        if fasca.f4 and iscrizione.corso4_id != None:
                            return redirect('errorefasciapiena')

                        if fasca.f5 and iscrizione.corso5_id != None:
                            return redirect('errorefasciapiena')

                        if fasca.f6 and iscrizione.corso6_id != None:
                            return redirect('errorefasciapiena')

                        if fasca.f7 and iscrizione.corso7_id != None:
                            return redirect('errorefasciapiena')

                        if fasca.f8 and iscrizione.corso8_id != None:
                            return redirect('errorefasciapiena')

                        if fasca.f9 and iscrizione.corso9_id != None:
                            return redirect('errorefasciapiena')




                        if fasca.f1 and iscrizione.corso1_id== None:
                            iscrizione.corso1 = fasca
                        if fasca.f2 and iscrizione.corso2_id== None:
                            iscrizione.corso2 = fasca
                        if fasca.f3 and iscrizione.corso3_id== None:
                            iscrizione.corso3= fasca
                        if fasca.f4 and iscrizione.corso4_id== None:
                            iscrizione.corso4= fasca
                        if fasca.f5 and iscrizione.corso5_id== None:
                            iscrizione.corso5= fasca
                        if fasca.f6 and iscrizione.corso6_id== None:
                            iscrizione.corso6= fasca
                        if fasca.f7 and iscrizione.corso7_id== None:
                            iscrizione.corso7= fasca
                        if fasca.f8 and iscrizione.corso8_id== None:
                            iscrizione.corso8= fasca
                        if fasca.f9 and iscrizione.corso9_id== None:
                            iscrizione.corso9= fasca
                    else:
                        return redirect('errore')


                else:
                    if contatore<classe_max:
                        if fasca.f1 and singoli=='f1' and iscrizione.corso1_id == None:
                            iscrizione.corso1_id = fasca
                        elif fasca.f2 and singoli=='f2' and iscrizione.corso2_id == None:
                            iscrizione.corso2_id = fasca
                        elif fasca.f3 and singoli=='f3' and iscrizione.corso3_id == None:
                            iscrizione.corso3_id= fasca
                        elif fasca.f4 and singoli=='f4' and iscrizione.corso4_id == None:
                            iscrizione.corso4_id= fasca
                        elif fasca.f5 and singoli=='f5' and iscrizione.corso5_id == None:
                            iscrizione.corso5_id= fasca
                        elif fasca.f6 and singoli=='f6' and iscrizione.corso6_id == None:
                            iscrizione.corso6_id= fasca
                        elif fasca.f7 and singoli=='f7' and iscrizione.corso7_id == None:
                            iscrizione.corso7_id= fasca
                        elif fasca.f8 and singoli=='f8' and iscrizione.corso8_id == None:
                            iscrizione.corso8_id= fasca
                        elif fasca.f9 and singoli=='f9' and iscrizione.corso9_id == None:
                            iscrizione.corso9_id= fasca
                    else:
                        return redirect('errore')


            iscrizione.save()
            return redirect('privata')

        else:
            form = IscrizioneForm(instance= iscrizione)


        return render(request, 'corsi/edit.html', {'form':form, 'corsi':corsi, 'contatore':contatore, 'tabellagrafica':tabellagrafica, 'iscrizione':iscrizione})



@login_required(login_url='/login/')
def filtro_fasce(request):

    pieno="0"
    corsi=request.GET.get("f")
    form = CercaCorsi(request.GET)
    cerca = request.GET.get("q")



    if corsi == 'f1':
        corsi = Corso.objects.filter(f1=True).order_by('titolo')
        fascia= 'f1'
    if corsi == 'f2':
        corsi = Corso.objects.filter(f2=True).order_by('titolo')
        fascia= 'f2'
    if corsi == 'f3':
        corsi = Corso.objects.filter(f3=True).order_by('titolo')
        fascia= 'f3'
    if corsi == 'f4':
        corsi = Corso.objects.filter(f4=True).order_by('titolo')
        fascia= 'f4'
    if corsi == 'f5':
        corsi = Corso.objects.filter(f5=True).order_by('titolo')
        fascia= 'f5'
    if corsi == 'f6':
        corsi = Corso.objects.filter(f6=True).order_by('titolo')
        fascia= 'f6'
    if corsi == 'f7':
        corsi = Corso.objects.filter(f7=True).order_by('titolo')
        fascia= 'f7'
    if corsi == 'f8':
        corsi = Corso.objects.filter(f8=True).order_by('titolo')
        fascia= 'f8'
    if corsi == 'f9':
        corsi = Corso.objects.filter(f9=True).order_by('titolo')
        fascia= 'f9'


    # if form.is_valid():
    #     if fascia== 'f1':
    #         corsi = Corso.objects.filter(Q(titolo__icontains=cerca)|
    #         Q(descrizione__icontains=cerca))

    return render(request, 'corsi/filtro_fasce.html', {'corsi' : corsi, 'fascia': fascia, 'form':form})

@login_required(login_url='/login/')
def elimina(request, corso_id):

    corsi = Corso.objects.filter( pk=corso_id)
    fasca = Corso.objects.get( pk=corso_id)
    tabella= Iscrizione.objects.filter(user=request.user)
    iscrizione=get_object_or_404(Iscrizione, pk=tabella)
    classe_max= fasca.aule.max_iscritti
    singoli=request.GET.get("f")

    if request.method == "POST":
        form = IscrizioneForm(request.POST, instance= iscrizione)


        if form.is_valid():
            iscrizione = form.save(commit=False)
            iscrizione.user = request.user
            iscrizione.published_date = timezone.now()
            if fasca.progressivo:

                if fasca.f1:
                    iscrizione.corso1_id = ''
                if fasca.f2:
                    iscrizione.corso2_id = ''
                if fasca.f3:
                    iscrizione.corso3_id= ''
                if fasca.f4:
                    iscrizione.corso4_id= ''
                if fasca.f5:
                    iscrizione.corso5_id= ''
                if fasca.f6:
                    iscrizione.corso6_id= ''
                if fasca.f7:
                    iscrizione.corso7_id= ''
                if fasca.f8:
                    iscrizione.corso8_id= ''
                if fasca.f9:
                    iscrizione.corso9_id= ''
            else:

                if fasca.f1 and singoli=='f1':
                    iscrizione.corso1_id = ''
                elif fasca.f2 and singoli=='f2':
                    iscrizione.corso2_id = ''
                elif fasca.f3 and singoli=='f3':
                    iscrizione.corso3_id= ''
                elif fasca.f4 and singoli=='f4':
                    iscrizione.corso4_id= ''
                elif fasca.f5 and singoli=='f5':
                    iscrizione.corso5_id= ''
                elif fasca.f6 and singoli=='f6':
                    iscrizione.corso6_id= ''
                elif fasca.f7 and singoli=='f7':
                    iscrizione.corso7_id= ''
                elif fasca.f8 and singoli=='f8':
                    iscrizione.corso8_id= ''
                elif fasca.f9 and singoli=='f9':
                    iscrizione.corso9_id= ''
                else:
                    return redirect('privata')


        iscrizione.save()
        return redirect('privata')

    else:
        form = IscrizioneForm(instance= iscrizione)

    return render(request, 'corsi/elimina.html', {'form':form, 'corsi':corsi})


def help(request):
    if request.method == "POST":
        form = Mail(request.POST)
        if form.is_valid():
            subject, from_email, to = form.cleaned_data['mail'], 'settimanaflessibile@gmail.com', 'settimanaflessibile@gmail.com'
            text_content = '456'
            html_content =  form.cleaned_data['testo']
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send(fail_silently=False)
            return redirect('successo')
    else:
        form = Mail()
    return render(request, 'corsi/help.html', {'form': form})
