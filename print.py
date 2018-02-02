#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
    
    from django.core.management import execute_from_command_line
    
    execute_from_command_line(sys.argv)

import math
import string
from django.contrib.auth.models import User
from app.models import Iscrizione
from app.models import Corso
from django.shortcuts import get_object_or_404


r=0
riga = 0
while riga < 400:
    riga = riga + 1
    try:
      corsi= Corso.objects.get(id= riga)
      f1=("Ven 1-2", (list(Iscrizione.objects.filter(corso9_id=corsi.id).values_list('user__username', flat=True))))
      iscritti= (Iscrizione.objects.filter(corso9_id=corsi.id))
      counter= iscritti.count()
      if counter != 0:
        r= r+1
        print(r,corsi)
        print("GLI STUDENTI DELLE CLASSI DEL BIENNIO CHE SONO AUTORIZZATE AD USCIRE ALLE 12:50 SONO LE SEGUENTI:")
        print("1 A-E-F-H")
        print("2 D-F-G-H-I-L-M-O-P")
        print(f1)
        print("_______________________________________________________________")

                   
                   
                   
    except:
      pass


