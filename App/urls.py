#importaciones ---------------------------------
from django.urls import path
from App import views
#importacion de vistas-------------


#code ------------------------------------------
urlpatterns = [
    #vistas-------------------------------------
    path('', views.inicio, name='inicio'),
    path('cursos/', views.cursos, name='cursos'),
    path('profesores/', views.profesores, name="profesores"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('estudiantesformulario/', views.estudiantesFormulario, name="estudiantesformulario"),
    path('estudiantesbuscador/', views.estudiantesBuscador, name="estudiantesBuscador"),
    path('buscarestudiantes/', views.buscarEstudiantes),
]