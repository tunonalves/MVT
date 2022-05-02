from django.shortcuts import render
from django.http import HttpResponse
from .models import family
from django.template import loader

# Create your views here.
def familiares(request):
    lista = [family.name,family.lastname,family.parent,family.dni]
    dicc2 = {'lista':lista}
    #diccionario = {'Nombre':family.name,'Apellido':family.lastname,'Parentesco':family.parent,'DNI':family.dni}
    plantilla = loader.get_template("familiares.html")
    documento = plantilla.render(dicc2)
    return HttpResponse(documento)

def inicio(request):
    plantilla = loader.get_template("index.html")
    documento = plantilla.render()
    return HttpResponse(documento)