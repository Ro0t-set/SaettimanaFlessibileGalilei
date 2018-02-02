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



riga = 0
while riga < 1425:
	riga = riga + 1
	print (riga)
	try:
		iscritti= Iscrizione.objects.get(id= riga)
		contatore1= Iscrizione.objects.filter(corso7_id=84)
		count= contatore1.count()
		if count > 31:
			if iscritti.corso7_id== 84:
				iscritti.corso7_id = None
				iscritti.save()
				print(funge)

	except:
		pass
