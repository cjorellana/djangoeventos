from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Contacto


class CustomUserCreationForm(UserCreationForm):
    pass

class ContactoForm(forms.ModelForm):
    """
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={
                "class" : "form-control",
                "placeholder": "Ingrese su nombre"
            }
        )
    )

    correo = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ingrese su Correo"
        }
        )
    )

    """

    class Meta:

        model=Contacto
        fields = ["nombre","correo","tipo","mensaje"]
        #fields='__all__'
