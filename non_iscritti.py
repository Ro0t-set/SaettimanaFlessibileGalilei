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

fascia = int(input("fascia [1-9]:"))



if fascia== 1:
	riga = 0
	while riga < 1425:
		riga = riga + 1
		percentuale= int((100*riga)/1425)
		try:
			iscritti= Iscrizione.objects.get(id= riga)
			if iscritti.user.is_staff:
				pass
				#print (" \033[1;33;40m salto utente:", iscritti)


			elif  iscritti.corso1_id ==None:#da corso1 a corso9
				#print(percentuale, "%","\033[1;32;40m ok ")
				corso = 0
					
				while corso < 300:
					corso = corso + 1
					try:
						corsi= Corso.objects.get(id= corso)
						if corsi.f1:  #da f1 a f9
							contatore1= Iscrizione.objects.filter(corso1_id=corsi) #da corso1 a corso9
							n_max= corsi.aule.max_iscritti
							contatore=contatore1.count()
							if contatore<n_max:
								iscritti.corso1_id= corsi #da corso1 a corso9
								iscritti.save()
								corso = 301

					except Corso.DoesNotExist:
						pass
		except Iscrizione.DoesNotExist:
			pass


	null_iscriitti= Iscrizione.objects.filter(corso1_id= None)#da corso1 a corso9
	null_iscriitt= null_iscriitti.count()

	print (" \033[1;31;40m persone non iscritte a nulla 1=",null_iscriitt)



#elif fascia== 2:
	riga = 0
	while riga < 1425:
		riga = riga + 1
		percentuale= int((100*riga)/1425)
		try:
			iscritti= Iscrizione.objects.get(id= riga)
			if iscritti.user.is_staff:
				pass
				#print (" \033[1;33;40m salto utente:", iscritti)


			elif  iscritti.corso2_id ==None:#da corso1 a corso9
				#print(percentuale, "%","\033[1;32;40m ok ")
				corso = 0
					
				while corso < 300:
					corso = corso + 1
					try:
						corsi= Corso.objects.get(id= corso)
						if corsi.f2:  #da f1 a f9
							contatore1= Iscrizione.objects.filter(corso2_id=corsi) #da corso1 a corso9
							n_max= corsi.aule.max_iscritti
							contatore=contatore1.count()
							if contatore<n_max:
								iscritti.corso2_id= corsi #da corso1 a corso9
								iscritti.save()
								corso = 301

					except Corso.DoesNotExist:
						pass
		except Iscrizione.DoesNotExist:
			pass


	null_iscriitti= Iscrizione.objects.filter(corso2_id= None)#da corso1 a corso9
	null_iscriitt= null_iscriitti.count()

	print (" \033[1;31;40m persone non iscritte a nulla 2=",null_iscriitt)

#elif fascia== 3:
	riga = 0
	while riga < 1425:
		riga = riga + 1
		percentuale= int((100*riga)/1425)
		try:
			iscritti= Iscrizione.objects.get(id= riga)
			if iscritti.user.is_staff:
				pass
				#print (" \033[1;33;40m salto utente:", iscritti)


			elif  iscritti.corso3_id ==None:#da corso1 a corso9
				#print(percentuale, "%","\033[1;32;40m ok ")
				corso = 0
					
				while corso < 300:
					corso = corso + 1
					try:
						corsi= Corso.objects.get(id= corso)
						if corsi.f3:  #da f1 a f9
							contatore1= Iscrizione.objects.filter(corso3_id=corsi) #da corso1 a corso9
							n_max= corsi.aule.max_iscritti
							contatore=contatore1.count()
							if contatore<n_max:
								iscritti.corso3_id= corsi #da corso1 a corso9
								iscritti.save()
								corso = 301

					except Corso.DoesNotExist:
						pass
		except Iscrizione.DoesNotExist:
			pass


	null_iscriitti= Iscrizione.objects.filter(corso3_id= None)#da corso1 a corso9
	null_iscriitt= null_iscriitti.count()

	print (" \033[1;31;40m persone non iscritte a nulla 3=",null_iscriitt)

#elif fascia== 4:
	riga = 0
	while riga < 1425:
		riga = riga + 1
		percentuale= int((100*riga)/1425)
		try:
			iscritti= Iscrizione.objects.get(id= riga)
			if iscritti.user.is_staff:
				pass
				#print (" \033[1;33;40m salto utente:", iscritti)


			elif  iscritti.corso4_id ==None:#da corso1 a corso9
				#print(percentuale, "%","\033[1;32;40m ok ")
				corso = 0
					
				while corso < 300:
					corso = corso + 1
					try:
						corsi= Corso.objects.get(id= corso)
						if corsi.f4:  #da f1 a f9
							contatore1= Iscrizione.objects.filter(corso4_id=corsi) #da corso1 a corso9
							n_max= corsi.aule.max_iscritti
							contatore=contatore1.count()
							if contatore<n_max:
								iscritti.corso4_id= corsi #da corso1 a corso9
								iscritti.save()
								corso = 301

					except Corso.DoesNotExist:
						pass
		except Iscrizione.DoesNotExist:
			pass


	null_iscriitti= Iscrizione.objects.filter(corso4_id= None)#da corso1 a corso9
	null_iscriitt= null_iscriitti.count()

	print (" \033[1;31;40m persone non iscritte a nulla 4=",null_iscriitt)

#elif fascia== 5:
	riga = 0
	while riga < 1425:
		riga = riga + 1
		percentuale= int((100*riga)/1425)
		try:
			iscritti= Iscrizione.objects.get(id= riga)
			if iscritti.user.is_staff:
				pass
				#print (" \033[1;33;40m salto utente:", iscritti)


			elif  iscritti.corso5_id ==None:#da corso1 a corso9
				#print(percentuale, "%","\033[1;32;40m ok ")
				corso = 0
					
				while corso < 300:
					corso = corso + 1
					try:
						corsi= Corso.objects.get(id= corso)
						if corsi.f5:  #da f1 a f9
							contatore1= Iscrizione.objects.filter(corso5_id=corsi) #da corso1 a corso9
							n_max= corsi.aule.max_iscritti
							contatore=contatore1.count()
							if contatore<(n_max+1):
								iscritti.corso5_id= corsi #da corso1 a corso9
								iscritti.save()
								corso = 301

					except Corso.DoesNotExist:
						pass
		except Iscrizione.DoesNotExist:
			pass


	null_iscriitti= Iscrizione.objects.filter(corso5_id= None)#da corso1 a corso9
	null_iscriitt= null_iscriitti.count()

	print (" \033[1;31;40m persone non iscritte a nulla 5=",null_iscriitt)

#elif fascia== 6:
	riga = 0
	while riga < 1425:
		riga = riga + 1
		percentuale= int((100*riga)/1425)
		try:
			iscritti= Iscrizione.objects.get(id= riga)
			if iscritti.user.is_staff:
				pass
				#print (" \033[1;33;40m salto utente:", iscritti)


			elif  iscritti.corso6_id ==None:#da corso1 a corso9
				#print(percentuale, "%","\033[1;32;40m ok ")
				corso = 0
					
				while corso < 300:
					corso = corso + 1
					try:
						corsi= Corso.objects.get(id= corso)
						if corsi.f6:  #da f1 a f9
							contatore1= Iscrizione.objects.filter(corso6_id=corsi) #da corso1 a corso9
							n_max= corsi.aule.max_iscritti
							contatore=contatore1.count()
							if contatore<(n_max+1):
								iscritti.corso6_id= corsi #da corso1 a corso9
								iscritti.save()
								corso = 301

					except Corso.DoesNotExist:
						pass
		except Iscrizione.DoesNotExist:
			pass


	null_iscriitti= Iscrizione.objects.filter(corso6_id= None)#da corso1 a corso9
	null_iscriitt= null_iscriitti.count()

	print (" \033[1;31;40m persone non iscritte a nulla 6=",null_iscriitt)

elif fascia== 7:
	riga = 0
	while riga < 1425:
		riga = riga + 1
		percentuale= int((100*riga)/1425)
		try:
			iscritti= Iscrizione.objects.get(id= riga)
			if iscritti.user.is_staff:
				pass
				#print (" \033[1;33;40m salto utente:", iscritti)


			elif  iscritti.corso7_id ==None:#da corso1 a corso9
				#print(percentuale, "%","\033[1;32;40m ok ")
				corso = 0
					
				while corso < 300:
					corso = corso + 1
					try:
						corsi= Corso.objects.get(id= corso)
						if corsi.f7:  #da f1 a f9
							contatore1= Iscrizione.objects.filter(corso7_id=corsi) #da corso1 a corso9
							n_max= corsi.aule.max_iscritti
							contatore=contatore1.count()
							if contatore<(n_max+1):
								iscritti.corso7_id= corsi #da corso1 a corso9
								iscritti.save()
								corso = 301

					except Corso.DoesNotExist:
						pass
		except Iscrizione.DoesNotExist:
			pass


	null_iscriitti= Iscrizione.objects.filter(corso7_id= None)#da corso1 a corso9
	null_iscriitt= null_iscriitti.count()

	print (" \033[1;31;40m persone non iscritte a nulla 7=",null_iscriitt)

#elif fascia== 8:
	riga = 0
	while riga < 1425:
		riga = riga + 1
		percentuale= int((100*riga)/1425)
		try:
			iscritti= Iscrizione.objects.get(id= riga)
			if iscritti.user.is_staff:
				pass
				#print (" \033[1;33;40m salto utente:", iscritti)


			elif  iscritti.corso8_id ==None:#da corso1 a corso9
				#print(percentuale, "%","\033[1;32;40m ok ")
				corso = 0
					
				while corso < 300:
					corso = corso + 1
					try:
						corsi= Corso.objects.get(id= corso)
						if corsi.f8:  #da f1 a f9
							contatore1= Iscrizione.objects.filter(corso8_id=corsi) #da corso1 a corso9
							n_max= corsi.aule.max_iscritti
							contatore=contatore1.count()
							if contatore<(n_max+2):
								iscritti.corso8_id= corsi #da corso1 a corso9
								iscritti.save()
								corso = 301

					except Corso.DoesNotExist:
						pass
		except Iscrizione.DoesNotExist:
			pass


	null_iscriitti= Iscrizione.objects.filter(corso8_id= None)#da corso1 a corso9
	null_iscriitt= null_iscriitti.count()

	print (" \033[1;31;40m persone non iscritte a nulla 8=",null_iscriitt)





#elif fascia== 9:
	riga = 0
	while riga < 1425:
		riga = riga + 1
		percentuale= int((100*riga)/1425)
		try:
			iscritti= Iscrizione.objects.get(id= riga)
			if iscritti.user.is_staff:
				pass
				#print (" \033[1;33;40m salto utente:", iscritti)


			elif  iscritti.corso9_id ==None:#da corso1 a corso9
				#print(percentuale, "%","\033[1;32;40m ok ")
				corso = 0
					
				while corso < 300:
					corso = corso + 1
					try:
						corsi= Corso.objects.get(id= corso)
						if corsi.f9:  #da f1 a f9
							contatore1= Iscrizione.objects.filter(corso9_id=corsi) #da corso1 a corso9
							n_max= corsi.aule.max_iscritti
							contatore=contatore1.count()
							if contatore<(n_max+1):
								iscritti.corso9_id= corsi #da corso1 a corso9
								iscritti.save()
								corso = 301

					except Corso.DoesNotExist:
						pass
		except Iscrizione.DoesNotExist:
			pass


	null_iscriitti= Iscrizione.objects.filter(corso9_id= None)#da corso1 a corso9
	null_iscriitt= null_iscriitti.count()

	print (" \033[1;31;40m persone non iscritte a nulla 9=",null_iscriitt)



















# null_iscriitti= list(Iscrizione.objects.get(corso1_id= None))

# for count in null_iscriitti:
# 	print (count)



# print (null_iscriitt)





	

# 	#corsi= Corso.objects.get(id= corso)
# 	corsi = get_object_or_404(Corso, id= corso)


# 	if corsi.f1:
# 		contatore1= Iscrizione.objects.filter(corso1_id=corsi)
# 		contatore=contatore1.count()
# 		print (contatore)









# corso=0
# while corso < 300:
# 	corso = corso + 1
# 	try:
# 		corsi= Corso.objects.get(id= corso)
# 		if corsi.f2:
# 			contatore1= Iscrizione.objects.filter(corso2_id=corsi)
# 			contatore=contatore1.count()
# 			corsi= 
# 			print(contatore)
# 	except Corso.DoesNotExist:
# 		print(".")




# fasca = Corso.objects.get( id=corso)
# contatore1= Iscrizione.objects.filter(corso1_id=fasca)
# contatore=contatore1.count()



# riga = 0
# while riga < 1420:
# 	riga = riga + 1







# # characters =  string.digits
# # riga = 0
# # while riga < 1417:
# #         riga = riga + 1
# #         excel_document = openpyxl.load_workbook('listautenti.xlsx')
# #         sheet = excel_document.get_sheet_by_name('Foglio1')
# #         nome_utente= (sheet.cell(row = riga, column = 1).value)
# #         classe= (sheet.cell(row = riga, column = 2).value)
# #         utente=(nome_utente+classe)
# #         print (riga)
# #         utente = User.objects.get(username=utente)
# #         Iscrizione.objects.create(user=utente)
