from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

from . import views

app_name = 'retoshuellascarbono'
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.CustomLoginView.as_view(),name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('registro/', views.registrarusuario, name = 'registro'),
    path('arte/', views.arte, name= 'arte'),
    path('add_poem/', views.subir_poema, name = 'poemas_form'),
    path('add_draw/', views.subir_dibujo, name='add_draw'),
    path('respuestaretos_form/<int:reto_id>/', views.respuestas_usuarios, name='respuestas_form'),
    path('administrar_retos_respuestas/', views.administrar_respuestas , name='administrar_respuestas'),
    path('ranking/', views.ranking, name='ranking'),
    path('crear_reto/', views.crear_reto, name='crear_reto'),
]

