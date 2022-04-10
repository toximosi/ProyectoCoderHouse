#Importaciones ----------------------------
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from App.migrations import Model

#Code--------------------------------------
def saludo(request):
    return HttpResponse("Hola Django - Code")

def index(self):
    index = Model(title='index')
    #papa.save()
    diccionario = {'index': index}
    
    template = loader.get_template('index.html')
    doc = template.render(diccionario)


    return HttpResponse()