from django.db import models

class Persona(models.Model):
    nombre= models.CharField(max_length=40)
    apellido= models.CharField(max_length=40)
    edad= models.IntegerField()
    parentesco= models.CharField(max_length=40)
    def __str__(self):
        return self.nombre