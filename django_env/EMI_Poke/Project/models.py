from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    catchphrase = models.CharField(max_length=300)

    def __str__(self):
        return self.name
