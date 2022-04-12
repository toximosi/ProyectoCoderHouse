from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from App.forms import CursoFormulario, EstudiantesFormulario, ProfesoresFormulario, EntregablesFormulario
from App.models import Cursos, Estudiantes, Profesores, Entregables

# Create your views here.

#Code--------------------------------------
#Paginas----------------------
def parent(request):
    return render(request, 'parent.html')

def inicio(request):
    return render(request, 'inicio.html')

def cursos(request):
    return render(request, 'cursos.html')

def profesores(request):
    return render(request, 'profesores.html')

def profesoresFormulario(request):
    return render(request, 'profesoresFormulario.html')

def estudiantes(request):
    return render(request, 'estudiantes.html')

def entregables(request):
    return render(request, 'entregables.html')

def entregablesFormulario(request):
    return render(request, 'entregablesFormulario.html')

#Formulario------------------
def cursosFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Cursos(nombre=informacion['nombre'], fechaDeInicio = informacion['fechaInicio'])
            curso.save()
            return render(request,"cursos.html")
    else:
        miFormulario = CursoFormulario()
    return render(request,"cursoFormulario.html", {"miFormulario":miFormulario})

def estudiantesFormulario(request):
    if request.method == 'POST':
        miFormulario = EstudiantesFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            estudiante = Estudiantes(nombre=informacion['nombre'], apellido = informacion['apellido'], curso = informacion['curso'])
            estudiante.save()
            return render(request,"estudiantes.html")
    else:
        miFormulario = EstudiantesFormulario()
    return render(request,"estudiantesFormulario.html", {"miFormulario":miFormulario})

def profesoresFormulario(request):
    if request.method == 'POST':
        miFormulario = ProfesoresFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            estudiante = profesores(nombre=informacion['nombre'], apellido = informacion['apellido'], curso = informacion['curso'])
            estudiante.save()
            return render(request,"profesores.html")
    else:
        miFormulario = profesoresFormulario()
    return render(request,"profesoresFormulario.html", {"miFormulario":miFormulario})



""" def estudiantesBuscador(request):

    respuesta = f"Estoy buscando el estudiante nro: {request.GET['nombre']}"
    return HttpResponse(respuesta) """
#bien----------------------------------------------------------INICIO
def estudiantesBuscador(request):
        return render(request, "estudiantesBuscador.html")

""" def buscar(request):

    respuesta = f"Estoy buscando el estudiante nro: {request.GET['nombre']}"
    return HttpResponse(respuesta) """
#bien----------------------------------------------------------FIN

def buscar(request):

    if request.GET["fname"]:
        nombre =request.GET['fname']
        estudiantes = Estudiantes.objects.filter(nombre__icontains=nombre)
        return render(request, "estudiantesResultado.html", {"estudiantes":estudiantes, "query":nombre })
    else:
        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)


def estudiantesBuscador(request):

    return render(request, "estudiantesBuscador.html",)

def estudiantesTodos(request):
    estudianteLista = Estudiantes.objects
    return render(request, estudianteLista)







""" def estudiantesBuscador(request):
    if request.GET['nombre']:
        nombre = request.GET['nombre']
        print(nombre)
        estudiantes = Estudiantes.objects.filter(nombre__icontains = nombre)
        print(estudiantes)
        return render(request, "App/estudiantesBuscador.html", {"nombre":estudiantes.nombre, "apellido":estudiantes.apellido, "curso":estudiantes.curso})
    else:
        respuesta = "No enviaste datos"

    return render(request, "App/estudiantesBuscador.html", {"respuesta":respuesta}) """