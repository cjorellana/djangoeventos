from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
                "class" : "form-control",
                "placeholder": "Ingrese su nombre"
            }
        )
    )

    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]

    def clean_email(self):
        Email = self.cleaned_data.get('email')
                
        if User.objects.filter(email=Email).exists():
            raise forms.ValidationError("El email ya se encuentra en uso")
        
        return Email