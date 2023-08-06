from django.shortcuts import render

def inicio(request):
    return render(request, "inicio.html")

def profesores(request):
    return render(request, "profesores.html")

def cursos(request):
    return render(request, "cursos.html")

def estudiantes(request):
    return render(request, "estudiantes.html")

def entregables(request):
    return render(request, "entregables.html")