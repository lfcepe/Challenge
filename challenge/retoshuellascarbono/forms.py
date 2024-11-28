from django import forms
from .models import Retosrespuesta, Dibujos, Poemas, Retos
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Reto_form (forms.ModelForm):
    class Meta:
        model: Retos
        fields = '__all__'
        widgets = {
            'reto': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion':forms.TextInput(attrs={'class': 'form-control'}),
            'puntos':forms.TextInput(attrs={'class': 'form-control'})
        }

class Retosrespuesta_form (forms.ModelForm):
    class Meta:
        model: Retosrespuesta
        fields= ['imagenusuario']
        widgets= {
            'imagenusuario':forms.ClearableFileInput(attrs={'class':'form-control'})
        }

class Poemas_form (forms.ModelForm):
    class Meta:
        model: Poemas
        fields = ['titulopoema', 'rima']
        widgets = {
            'titulopoema':forms.TextInput(attrs={'class': 'form-control'}),
            'rima':forms.TextInput(attrs={'class': 'form-control'}),
        }

class Dibujos_form (forms.ModelForm):
    class Meta:
        model: Dibujos
        fields = ['nombredibujo', 'imagen']
        widgets = {
            'nombredibujo':forms.TextInput(attrs={'class': 'form-control'}), 
            'imagen':forms.ClearableFileInput(attrs={'class':'form-control'}),
        }

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password_confirm']
        labels = {
            'username': 'Nombre de usuario', 
            'first_name':'Nombre', 
            'last_name': 'Apellido',
            'password': 'Contraseña',
            'password_confirm': 'Confirmar Contraseña',
        }

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        
        if password != password_confirm:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password_confirm