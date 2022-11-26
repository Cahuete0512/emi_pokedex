from django.db import models

class Person(models.Model):
    # Name = equipe_1 || equipe_2 || equipe_3 etc....
    name = models.CharField(max_length=30)

# TODO: Ajouter liste de Pokemon
    def __str__(self):
        return self.name



