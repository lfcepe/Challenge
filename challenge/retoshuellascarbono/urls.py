from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

app_name = 'retoshuellascarbono'
urlpatterns = [
    path('', views.index, name="index"),
    
]

