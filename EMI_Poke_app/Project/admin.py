from django.contrib import admin

from .models import Person
from .models import Pokemon
from .models import Equipe

admin.site.register(Person)
admin.site.register(Pokemon)
admin.site.register(Equipe)