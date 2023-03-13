from django.shortcuts import render,get_object_or_404
from .models import Evento,Persona,Pais
from datetime import datetime
from .forms import ContactoForm,CustomUserCreationForm

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

def registro(request):
    data ={
        'form': CustomUserCreationForm
    }
    return render(request,'usuarios/registro.html',data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Soporte Ingresado, Pronto nos comunicaremos"
        else:
            data["form"] = formulario


    return render(request, "contacto.html",data)