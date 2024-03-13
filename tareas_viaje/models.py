from django.db import models
from django.test import TestCase, Client

#Pruebas Unitarias
class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField()
    completada = models.BooleanField(default=False)
    categoria = models.CharField(max_length=50, choices=[
        ('transporte', 'Transporte'),
        ('alojamiento', 'Alojamiento'),
        ('actividades', 'Actividades Turísticas'),
        ('alimentacion', 'Alimentación'),
        ('gastos', 'Gastos Diversos'),
    ])

    def __str__(self):
        return self.titulo
    
#Pruebas Integrales
class TareaViewTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_vista_creacion_tarea(self):
        response = self.client.post('/crear_tarea', {
            'titulo': 'Tarea de prueba',
            'descripcion': 'Esta es una tarea de prueba',
            'fecha_limite': '2024-03-15',
            'hora_limite': '12:00',
            'categoria': 'prueba'
        })
        self.assertEqual(response.status_code, 200)
       