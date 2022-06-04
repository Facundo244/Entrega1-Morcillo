from django.http import HttpResponse
from django.shortcuts import render
from AppCoder import views
from django.template import loader



def sectores(self):
    plantilla = loader.get_template('AppCoder/sectores.html')
    documento = plantilla.render()
    return HttpResponse(documento)


def profesionales(self):
    plantilla = loader.get_template('AppCoder/profesionales.html')
    documento = plantilla.render()
    return HttpResponse(documento)


def turnos(self):
    plantilla = loader.get_template('AppCoder/turno.html')
    documento = plantilla.render()
    return HttpResponse(documento)



def inicio(self):
    plantilla = loader.get_template('AppCoder/inicio.html')
    documento = plantilla.render()
    return HttpResponse(documento)
