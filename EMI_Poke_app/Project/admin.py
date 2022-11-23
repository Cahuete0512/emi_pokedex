from django.contrib import admin

from .models import Person
from .models import Pokemon

admin.site.register(Person)
admin.site.register(Pokemon)