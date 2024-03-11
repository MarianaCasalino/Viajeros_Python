from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tareas, name='lista_tareas'),
    # Paths para las nuevas funcionalidades
    path('elaborar_presupuesto/', views.elaborar_presupuesto, name='elaborar_presupuesto'),
    path('diario_de_viaje/', views.diario_de_viaje, name='diario_de_viaje'),
    path('mapa/', views.mapa, name='mapa'),
]