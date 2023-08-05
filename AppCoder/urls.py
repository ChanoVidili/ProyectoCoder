from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    
    path('cursos/', views.index),
    #path('profesores/', views.profesores),
    #path('cursestudiantesos/', views.estudiantes),
    #path('entregables/', views.entregables),
    
]