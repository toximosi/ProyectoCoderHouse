#importaciones----------------------------
from django.contrib import admin
from .models import *

# Register your models here.
#Code---------------------------------
admin.site.register(Cursos)
admin.site.register(Estudiantes)
admin.site.register(Profesores)
admin.site.register(Entregables)