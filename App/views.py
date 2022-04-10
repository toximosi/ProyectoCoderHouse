from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
# Create your views here.

#Code--------------------------------------
def parent(request):
    return render(request, 'parent.html')

def inicio(request):
    return render(request, 'inicio.html')

def cursos(request):
    return render(request, 'cursos.html')

def profesores(request):
    return render(request, 'profesores.html')

def estudiantes(request):
    return render(request, 'estudiantes.html')

def entregables(request):
    return render(request, 'entregables.html')

