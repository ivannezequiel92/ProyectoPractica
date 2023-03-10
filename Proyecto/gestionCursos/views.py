from django.shortcuts import render
from gestionCursos.models import Curso
from django.http import HttpResponse
# Create your views here.

def guardar_curso(request, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()
    doc = f"El curso que va a comenzar es: {curso.nombre} del año : {curso.camada}"
    return HttpResponse(doc)