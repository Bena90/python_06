from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Template, Context
from .models import Persona


def saludo (request):
    return HttpResponse('Hello World!')

def familia (request):
    
    mihtml = open('C:/Users/Bena/Python/desafio_06/desafio_06/appFamilia/template/index.html')
    
    lista_de_familiares = Persona.objects.all()

    diccionario= { "familiares": lista_de_familiares}

    plantilla = Template(mihtml.read())

    mihtml.close()

    Contexto = Context(diccionario)

    documento  = plantilla.render(Contexto)

    return HttpResponse(documento)


