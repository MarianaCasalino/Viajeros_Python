from django.urls import path
from .views import home, registro_tarea, diario_de_viaje

urlpatterns = [
    path('', home, name='home'),
    path('registro_tarea/', registro_tarea, name='registro_tarea'),
    path('diario_de_viaje/', diario_de_viaje, name='diario_de_viaje'),
]