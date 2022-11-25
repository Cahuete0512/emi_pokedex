from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    catchphrase = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    speciesName = models.CharField(max_length=30)
    picture = models.CharField(max_length=100)
    types = models.CharField(max_length=30)
    abilities = models.CharField(max_length=30)
    weight = models.CharField(max_length=30)

    # Methode qui permet de différencier les objets entre eux.
    def __str__(self):
        return self.speciesName




