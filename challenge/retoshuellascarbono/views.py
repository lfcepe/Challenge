from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Retos, Retosrespuesta, Poemas, Dibujos, Rankings
from .forms import Retosrespuesta_form, 
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

<<<<<<< HEAD
#Vista para el login
class CustomLoginView(LoginView):
    template_name = 'login.html'
=======
def arte(request):
    
>>>>>>> 56d17cede78b9e6a7f04ad3808a93f154177d96c
