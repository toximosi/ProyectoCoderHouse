#importaciones------------------
from django import forms 

#code----------------------------
class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    #entregables = forms.IntegerField()
    fechaDeInicio = forms.DateField()
    #fechaDeFin = forms.DateField()
    #horario = forms.TimeField()

class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    curso = forms.CharField()

class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    curso = forms.CharField()

class EntregablesFormulario(forms.Form):
    nombre = forms.CharField()
    tipo = forms.CharField()
    fechaEntrega = forms.DateField()
    Nota = forms.IntegerField()