from django import forms
from .models import Contacto

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
