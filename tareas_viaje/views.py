from django.shortcuts import render
from .models import Tarea

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas_viaje/lista_tareas.html', {'tareas': tareas})

def diario_de_viaje(request):
    return render(request, 'tareas_viaje/diario_de_viaje.html')

def registro_tarea(request):
    return render(request, 'tareas_viaje/registro_tarea.html')

def home(request):
    return render(request, 'home.html')