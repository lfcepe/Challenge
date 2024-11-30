from django.template import loader
from django.http import HttpResponse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Retos, Retosrespuesta, Poemas, Dibujos, Rankings
from .forms import Retosrespuesta_form, Reto_form, Dibujos_form, Poemas_form, UserRegistrationForm

#  Create your views here.

def index(request):
    # Obtener todos los retos
    retos = Retos.objects.all()
    
    # Pasar los retos al contexto
    context = {'retos': retos}
    
    # Renderizar la plantilla con los datos
    return render(request, 'index.html', context)
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
            return redirect('retoshuellascarbono:login') 

    else:
        form = UserRegistrationForm()
    
    return render(request, 'registro.html', {'form': form})

@login_required
def subir_poema(request):
    usuario = request.user
    if request.method == 'POST':
        form = Poemas_form(request.POST)
        if form.is_valid():
            poema = form.save(commit=False)
            poema.usuario = usuario
            poema.save()
            poema.puntospoemas += 5
            ranking.puntostotales += poema.puntospoemas
            poema.save()
            return redirect('retoshuellascarbono:arte')  
    else:
        form = Poemas_form()
    return render(request, 'poemas_form.html', {'form': form})


@login_required
def subir_dibujo(request):
    usuario = request.user
    if request.method == 'POST':
        form = Dibujos_form(request.POST, request.FILES)
        if form.is_valid():
            dibujo = form.save(commit=False)
            dibujo.usuario = usuario
            dibujo.save()
            dibujo.puntosdibujo += 6
            ranking.puntostotales += dibujo.puntosdibujo
            dibujo.save()
            return redirect('retoshuellascarbono:arte')  
    else:
        form = Dibujos_form()
    return render(request, 'dibujos_form.html', {'form': form})

#retos
@login_required
def usuariosretos_form(request, reto_id=None):
    # Intenta obtener el reto con el ID proporcionado
    reto = reto_id
    
    if request.method == 'POST':
        form = Retosrespuesta_form(request.POST, request.FILES)
        if form.is_valid():
            reto_respuesta = form.save(commit=False)
            reto_respuesta.usuario = request.user
            reto_respuesta.reto = reto  # Asigna el reto obtenido
            reto_respuesta.save()
            return redirect('retoshuellascarbono:index')
    else:
        form = Retosrespuesta_form()

    return render(request, 'usuariosretos_form.html', {'form': form, 'reto': reto})

@login_required
def administrar_respuestas(request, reto_id):
    retos_respuestas = Retosrespuesta.objects.filter(estado='pendiente')
    if request.method == 'POST':
        reto_respuesta_id = request.POST.get('reto_respuesta_id')
        accion = request.POST.get('accion')
        reto_respuesta = Retosrespuesta.objects.get(id=reto_respuesta_id)

        if accion == 'aprobar':
            reto_respuesta.estado = 'APROVADO'
            reto_respuesta.save()
            reto = get_object_or_404(Retos, pk = reto_id)
            ranking, created = Rankings.objects.get_or_create(usuario=reto_respuesta.usuario)
            ranking.puntostotales += reto.puntos
            ranking.save()
        else:
            reto_respuesta.estado = 'RECHAZADO'
            reto_respuesta.save()
            ranking, created = Rankings.objects.get_or_create(usuario=reto_respuesta.usuario)
            ranking.puntostotales += 0
            ranking.save()


    return render(request, 'administrar_retos.html', {'retos_respuestas': retos_respuestas})

#ranking
def ranking(request):
    rankings = Rankings.objects.all().order_by('-puntostotales')
    return render(request, 'ranking.html', {'rankings': rankings})

@receiver(post_save, sender=User)
def crear_usuario_ranking(sender, instance, created, **kwargs):
    if created:
        Rankings.objects.create(user=instance)

def puntaje_usuario(request):
    if request.user.is_authenticated:
        ranking = Rankings.objects.get(user=request.user)
        return {'puntaje_total': ranking.puntostotales}
    return {}

#Retos Administradores
def es_administrador(user):
    return user.groups.filter(name='administradores').exists()

@login_required
@user_passes_test(es_administrador)
def crear_reto(request):
    if request.method == 'POST':
        form = Reto_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('retoshuellascarbono:index')  
    else:
        form = Reto_form()
    return render(request, 'retos_form.html', {'form': form})