from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from App.forms import CursoFormulario, EstudiantesFormulario, ProfesoresFormulario
from App.models import Cursos, Estudiantes, Profesores

# Create your views here.

#Code--------------------------------------
#Paginas----------------------
def parent(request):
    return render(request, 'parent.html')

def inicio(request):
    return render(request, 'inicio.html')

def profesores(request):
    profesorLista = Profesores.objects.all()
    return render(request, 'profesores.html', {"profesores":profesorLista})

def cursos(request):
    cursosLista = Cursos.objects.all()
    return render(request, 'cursos.html', {"cursos":cursosLista})

#Estudiante----------------------------------------------------------
def estudiantes(request):
    estudianteLista = Estudiantes.objects.all()
    return render(request, "estudiantes.html", {"estudiantes":estudianteLista})

def buscarEstudiantes(request):
    if request.GET["fname"]:
        nombre =request.GET['fname']
        estudiantes = Estudiantes.objects.filter(nombre__icontains=nombre)
        return render(request, "estudiantesResultado.html", {"estudiantes":estudiantes, "query":nombre })
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)

def estudiantesBuscador(request):
    return render(request, "estudiantesBuscador.html",)

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