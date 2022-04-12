#importaciones ---------------------------------
from django.urls import path
from App import views
#importacion de vistas-------------


#code ------------------------------------------
urlpatterns = [
    #path('admin/', admin.site.urls),
    #vistas-------------------------------------
    path('', views.inicio, name='inicio'),
    path('cursos/', views.cursos, name='cursos'),
    path('cursosformulario/', views.cursosFormulario, name='cursosFormulario'),
    path('profesores/', views.profesores, name="profesores"),
    path('profesoresformulario/', views.profesoresFormulario, name="profesoresFormulario"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('estudiantesformulario/', views.estudiantesFormulario, name="estudiantesformulario"),
    path('entregables/', views.entregables, name="entregables"),
    path('entregablesformulario/', views.entregablesFormulario, name="entregablesFormulario"),
    path('buscar/', views.buscar),
    path('estudiantesbuscador/', views.estudiantesBuscador, name="estudiantesBuscador"),
    path('buscar/', views.buscar),
]