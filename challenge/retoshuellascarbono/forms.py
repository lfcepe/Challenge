from django import forms
from models import Retosrespuesta, Dibujos, Poemas, Retos

class Reto_form (forms.ModelForm):
    class Meta:
        model: Retos
        fields: '___all__'
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