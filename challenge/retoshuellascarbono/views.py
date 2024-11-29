from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Retos, Retosrespuesta, Poemas, Dibujos, Rankings
from .forms import Retosrespuesta_form, Reto_form, Dibujos_form, Poemas_form, UserRegistrationForm
# Create your views here.

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

#Vista para el login
class CustomLoginView(LoginView):
    template_name = 'login.html'

def arte(request):
    poemas = Poemas.objects.all()  
    dibujos = Dibujos.objects.all()
    
    return render(request, 'arte.html', {
        'poemas': poemas,
        'dibujos': dibujos,
    })

def registrarusuario(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.set_password(form.cleaned_data['password'])
            usuario.save()
            from django.contrib.auth import login
            login(request, usuario)
            messages.success(request, "Tu cuenta se ha creado correctamente.")
            return redirect('login') 

    else:
        form = UserRegistrationForm()
    
    return render(request, 'registro.html', {'form': form})

@login_required
def subir_poema(request):
    usuario = User.objects.get(user=request.user)
    if request.method == 'POST':
        form = Poemas_form(request.POST)
        if form.is_valid():
            poema = form.save(commit=False)
            poema.usuario = usuario
            poema.save()
            poema.puntospoemas += 5
            poema.save()
            return redirect('arte')  # Redirige al apartado artístico
    else:
        form = Poemas_form()
    return render(request, 'poemas_form.html', {'form': form})


@login_required
def subir_dibujo(request):
    usuario = User.objects.get(user=request.user)
    if request.method == 'POST':
        form = Dibujos_form(request.POST, request.FILES)
        if form.is_valid():
            dibujo = form.save(commit=False)
            dibujo.usuario = usuario
            dibujo.save()
            dibujo.puntosdibujo += 6
            dibujo.save()
            return redirect('arte')  
    else:
        form = Dibujos_form()
    return render(request, 'dibujos_form.html', {'form': form})