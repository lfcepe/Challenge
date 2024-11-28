from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Retos, Retosrespuesta, Poemas, Dibujos, Rankings
from .forms import Retosrespuesta_form, Reto_form, Dibujos_form, Poemas_form
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

#Vista para el login
class CustomLoginView(LoginView):
    template_name = 'login.html'

def arte():
    pass
    
def arte(request):
    poemas = Poemas.objects.order_by('titulopoema')
    dibujos = Dibujos.objects.order_by('')
