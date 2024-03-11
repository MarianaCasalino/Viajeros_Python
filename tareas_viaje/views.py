from django.shortcuts import render
from .models import Tarea

def lista_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'tareas_viaje/lista_tareas.html', {'tareas': tareas})


def elaborar_presupuesto(request):
    return render(request, 'tareas_viaje/elaborar_presupuesto.html')


def diario_de_viaje(request):
    return render(request, 'tareas_viaje/diario_de_viaje.html')

def mapa(request):
    return render(request, 'tareas_viaje/mapa.html')

