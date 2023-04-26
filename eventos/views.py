from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views import View

from .models import Evento,Persona,Pais
from datetime import datetime
from .forms import ContactoForm

# Create your views here.

class EventosListView(ListView):
    fecha_actual= datetime.now()
    template_name='index.html'
    queryset = Evento.objects.filter(fin__gte=fecha_actual)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Eventos"
        context['listado'] = context['evento_list']

        return context


def index(request):

    fecha_actual= datetime.now()
    eventos = Evento.objects.filter(fin__gte=fecha_actual)
    #eventos = Evento.objects.all()

    data = {
        'titulo': "Eventos",
        'listado': eventos
    }

    return render(request,'index.html',data)

class detalle(DetailView):
    model = Evento
    template_name = 'detalle.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = "Detalle Evento"
        #print(context)
        return context


def detalle_old(request,codigo):
    #eventos = Evento.objects.get(id=codigo)
    eventos = get_object_or_404(Evento,id=codigo)

    data = {
        'titulo': "Detalle",
        'listado': eventos
    }
    return render(request,"detalle.html",data)


class contacto(View):
    template_name = 'contacto.html'
    def get(self, request):
        form = ContactoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Soporte ingresado, pronto nos comunicaremos")
            form = ContactoForm()
            return render(request, self.template_name, {'form': form})
        else:
            messages.error(request, "Hubo un error en el formulario")
            return render(request, self.template_name, {'form': form})


from .forms import ContactoForm

class ContactoView(FormView):
    template_name = "contacto.html"
    form_class = ContactoForm
    success_url = reverse_lazy('contacto')  # Reemplace 'contacto' con la URL de éxito que desee

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Soporte ingresado, pronto nos comunicaremos")
        form = self.form_class()
        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        messages.error(self.request, "Hubo un error en el formulario")
        return self.render_to_response(self.get_context_data(form=form))


def contacto_old(request):
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

def custom_404(request, exception):
    return render(request, '404.html', {})
