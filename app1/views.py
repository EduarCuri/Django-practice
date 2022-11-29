from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Familiar

# Create your views here.

def saludar(request):
    return HttpResponse("BIENVENIDO A LA PRIMERA VISTA")

def despedida(request):
    return HttpResponse("HASTA LUEGO DESDE LOS PRIMEROS REQUEST EN DJANGO")

def saludo_con_parametro(request, nombre, carrera):
    return HttpResponse(f'Bienvenido {nombre} y eres un {carrera} excelente')

def despedida_con_parametros(request, nombre, apellido, distrito):
    return HttpResponse(f'Hasta luego {nombre} {apellido}, nos vemos en {distrito}')

def primer_template(request):
    return render(request, "app1/index.html")

def segundo_template(request, nombreCompleto, especialidad):
    return render(request, "app1/index2.html",
    {
        "nombreCompleto" : nombreCompleto,
        "especialidad" : especialidad,
        "notas" : [1, 2, 3, 4, 5, 6]
    })

def monstrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "app1/familiares.html", 
    {
        "lista_familiares": lista_familiares
    })

