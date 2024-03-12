from django.test import TestCase
from .models import Tarea
from .forms import TareaForm
from django.urls import reverse


#Pruebas Unitarias
class TareaModelTestCase(TestCase):
    def test_tarea_creation(self):
        tarea = Tarea.objects.create(
            titulo='Prueba de Tarea',
            descripcion='Esta es una tarea de prueba',
            fecha_limite='2024-03-15 12:00',
            completada=False,
            categoria='actividades'
        )
        self.assertEqual(tarea.titulo, 'Prueba de Tarea')
        self.assertEqual(tarea.descripcion, 'Esta es una tarea de prueba')
        self.assertEqual(str(tarea), 'Prueba de Tarea')

class TareaFormTestCase(TestCase):
    def test_valid_form(self):
        form_data = {
            'titulo': 'Tarea de prueba',
            'descripcion': 'Esta es una tarea de prueba',
            'fecha_limite': '2024-03-15 12:00',
            'completada': False,
            'categoria': 'actividades'
        }
        form = TareaForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {}
        form = TareaForm(data=form_data)
        self.assertFalse(form.is_valid())

#Pruebas integrales
        
class TareasViajeIntegrationTestCase(TestCase):
    def test_creacion_tarea_y_redireccionamiento(self):
        # Simular la creación de una tarea a través del formulario
        response = self.client.post(reverse('elaborar_presupuesto'), {
            'titulo': 'Tarea de prueba',
            'descripcion': 'Esta es una tarea de prueba',
            'fecha_limite': '2024-03-15 12:00',
            'completada': False,
            'categoria': 'actividades'
        })
        self.assertEqual(response.status_code, 302)  # Redireccionamiento después de la creación

        # Verificar si la tarea se ha creado correctamente
        tarea_creada = Tarea.objects.get(titulo='Tarea de prueba')
        self.assertIsNotNone(tarea_creada)
        self.assertEqual(tarea_creada.descripcion, 'Esta es una tarea de prueba')

    def test_listado_tareas(self):
        # Crear algunas tareas de prueba
        Tarea.objects.create(
            titulo='Tarea 1',
            descripcion='Esta es la tarea número uno',
            fecha_limite='2024-03-15 12:00',
            completada=False,
            categoria='actividades'
        )
        Tarea.objects.create(
            titulo='Tarea 2',
            descripcion='Esta es la tarea número dos',
            fecha_limite='2024-03-20 12:00',
            completada=True,
            categoria='alojamiento'
        )

        # Acceder a la lista de tareas y verificar si las tareas creadas están presentes
        response = self.client.get(reverse('lista_tareas'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tarea 1')
        self.assertContains(response, 'Tarea 2')