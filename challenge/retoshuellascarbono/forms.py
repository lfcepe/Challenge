from django import forms
from .models import Retosrespuesta, Dibujos, Poemas, Retos
from django.contrib.auth.models import User

class Reto_form (forms.ModelForm):
    class Meta:
        model: Retos
        fields: '__all__'
        widgets: {
            'reto',
            'descripcion',
            'puntos',
        }

class Retosrespuesta_form (forms.ModelForm):
    class Meta:
        model: Retosrespuesta
        fields: ['imagenusuario']
        widgets:{
            'imagenusuario',
        }

class Poemas_form (forms.ModelForm):
    class Meta:
        model: Poemas
        fields:['titulopoema', 'rima']
        widgets:{
            'titulopoema',
            'rima',
        }

class Dibujos_form (forms.ModelForm):
    class Meta:
        model: Dibujos
        fields:['nombredibujo', 'imagen']
        widgets:{
            'nombredibujo', 
            'imagen',
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        
        if password != password_confirm:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password_confirm