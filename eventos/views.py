from django.shortcuts import render,get_object_or_404
from .models import Evento,Persona,Pais
from datetime import datetime

# Create your views here.

def index(request):

    fecha_actual= datetime.now()
    eventos = Evento.objects.filter(fin__gte=fecha_actual)
    #eventos = Evento.objects.all()


    data = {
        'titulo': "Eventos",
        'listado': eventos
    } 
    
    return render(request,'index.html',data)

def custom_404(request, exception):
    return render(request, '404.html', {})

def about(request):
    return render(request,"about.html")

def detalle(request,codigo):

    #eventos = Evento.objects.get(id=codigo)
    eventos = get_object_or_404(Evento,id=codigo)

    data = {
        'titulo': "Detalle",
        'listado': eventos       
    } 
    return render(request,"detalle.html",data)

    