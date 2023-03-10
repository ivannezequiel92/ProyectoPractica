from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
   
 return HttpResponse("Hola Ivan practicando su primer proyecto")

def probandoTemplate(self):
     nom = "Ivan"
     ap = "Barboza"
     diccionario = {"nombre":nom, "apellido":ap}
    
     miHtml = open(r'C:\Users\Ivan\OneDrive\Desktop\ProyectoPractica\ProyectoPractica1\Plantilas\template.html')
     plantilla = Template(miHtml.read())
    
     miHtml.close()
    
     miContexto = Context(diccionario)
     documento = plantilla.render(miContexto)
    
     return HttpResponse(documento)

def curso(self):
     curso = Curso(nombre="Desarrollo web", camada="19999")
     curso.save()
     documentoDetexto = f"---> {curso.nombre}  camada : {curso.camada}"
     
     return HttpResponse(documentoDetexto)