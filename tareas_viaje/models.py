from django.db import models

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