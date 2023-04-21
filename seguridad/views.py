from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate,login

from .forms import CustomUserCreationForm

# Create your views here.

class CustomLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return super().get(request, *args, **kwargs)

def registro(request):

    if request.user.is_authenticated:
        return redirect('index')

    data ={
        'form': CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(
                username=formulario.cleaned_data["username"],
                password=formulario.cleaned_data["password1"]
            )
            login(request, user)
            return redirect(to="index")

        data["form"] = formulario


    return render(request,'usuarios/registro.html',data)