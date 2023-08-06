from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('profesores/', views.profesores, name="Profesores"),
    path('cursos/', views.cursos, name="Cursos"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('entregables/', views.entregables, name="Entregables"),    
]