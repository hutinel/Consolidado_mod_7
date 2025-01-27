from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear datos de prueba
        cls.laboratorio = Laboratorio.objects.create(nombre='Laboratorio Test', ciudad='Test City', pais='Test Country')

    def test_laboratorio_nombre(self):
        # Verificar que el nombre del laboratorio sea el esperado
        self.assertEqual(self.laboratorio.nombre, 'Laboratorio Test')

    def test_laboratorio_ciudad(self):
        # Verificar que la ciudad del laboratorio sea la esperada
        self.assertEqual(self.laboratorio.ciudad, 'Test City')

    def test_laboratorio_pais(self):
        # Verificar que el país del laboratorio sea el esperado
        self.assertEqual(self.laboratorio.pais, 'Test Country')

class LaboratorioViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Crear datos de prueba
        cls.laboratorio = Laboratorio.objects.create(nombre='Laboratorio Test', ciudad='Test City', pais='Test Country')

    def test_laboratorio_list_view(self):
        # Verificar que la URL devuelva una respuesta HTTP 200
        response = self.client.get(reverse('laboratorio_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio/laboratorio_list.html')
        self.assertContains(response, 'Laboratorio Test')

    def test_laboratorio_index_view(self):
        # Verificar que la URL devuelva una respuesta HTTP 200 y use la plantilla `index.html`
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio/index.html')
        self.assertContains(response, 'Bienvenido') # Ajusta este contenido según lo que tenga tu plantilla index.html