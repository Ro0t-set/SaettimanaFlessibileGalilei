import string
from random import *
from django.contrib.auth.models import User

characters =  string.digits
password =  "".join(choice(characters) for x in range(randint(8, 8)))
print password

user=User.objects.create_user('foo', password='bar')
user.is_superuser=False
user.is_staff=False
user.save()