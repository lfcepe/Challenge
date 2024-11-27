from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

from . import views

app_name = 'retoshuellascarbono'
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.CustomLoginView.as_view(),name="login"),
    path('logout/', LogoutView.as_view(), name="logout")
    
]

