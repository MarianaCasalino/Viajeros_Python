from django.test import TestCase
from django.utils import timezone
from .models import Tarea

class TareaUnitariaTest(TestCase):
    def test_creacion_tarea(self):
        tarea = Tarea.objects.create(
            titulo='Tarea de prueba',
            descripcion='Descripción de prueba',
            fecha_limite=timezone.now(),
            categoria='transporte'
        )
        self.assertEqual(str(tarea), tarea.titulo)
        self.assertFalse(tarea.completada)

    def test_completar_tarea(self):
        tarea = Tarea.objects.create(
            titulo='Tarea a completar',
            descripcion='Descripción de tarea a completar',
            fecha_limite=timezone.now(),
            categoria='alojamiento'
        )
        tarea.completada = True
        tarea.save()
        tarea_actualizada = Tarea.objects.get(pk=tarea.pk)
        self.assertTrue(tarea_actualizada.completada)

class TareaIntegralTest(TestCase):
    def test_creacion_tarea_y_completado(self):
        tarea = Tarea.objects.create(
            titulo='Tarea integral de prueba',
            descripcion='Descripción de prueba para tarea integral',
            fecha_limite=timezone.now(),
            categoria='actividades'
        )
        self.assertEqual(str(tarea), tarea.titulo)
        self.assertFalse(tarea.completada)

        tarea.completada = True
        tarea.save()
        tarea_actualizada = Tarea.objects.get(pk=tarea.pk)
        self.assertTrue(tarea_actualizada.completada)
