from django.shortcuts import render
from django.http import HttpResponse
from .models import Evento,Persona,Pais


# Create your views here.

def index(request):

    eventos = Evento.objects.all()

    data = {
        'titulo': "Eventos",
        'listado': eventos
    } 
    
    return render(request,'index.html',data)
    
def about(request):
    return render(request,"about.html")


    