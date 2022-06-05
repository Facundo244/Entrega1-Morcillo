from django.http import HttpResponse
from django.shortcuts import render
from AppCoder import views
from django.template import loader
from AppCoder.models import Sector
from AppCoder.forms import SectorFormulario



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


def sectoresFormulario(request):


    if request.method == 'POST':

        miFormulario = SectorFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data


        nombre = informacion['nombre']
        profesion = informacion['profesion']

        sector = Sector(nombre=nombre, profesion=profesion)
        sector.save()

        return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario = SectorFormulario()
        
    return render(request, 'AppCoder/sectoresFormulario.html', {'miFormulario':miFormulario})


def busquedaSector(request):
    return render(request, 'AppCoder/busquedaSector.html')


def buscar(request):

    if request.GET["sector"]:
        sector= request.GET['sector']
        sectores = Sector.objects.filter(nombre=sector)
        return render(request, 'AppCoder/resultadosBusqueda.html' , {'sector': sector,'sectores':sectores})
    else:
        respuesta = "No se ingreso ningun sector existente"
        return HttpResponse(respuesta)







#def buscar(request):
    #respuesta = f"Estoy buscando el sector {request.GET['sector']}"
    #return HttpResponse(respuesta)
