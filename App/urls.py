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
    path('profesores/', views.profesores, name="profesores"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('entregables/', views.entregables, name="entregables"),
]