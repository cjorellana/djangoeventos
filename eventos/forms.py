from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model=Contacto
        fields = ["nombre","correo","tipo","mensaje"]
        #fields='__all__'
