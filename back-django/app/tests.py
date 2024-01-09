from django.test import TestCase
from .models import MyModel

class MyModelTestCase(TestCase):
    def setUp(self):
        MyModel.objects.create(name="test")

    def test_model_can_create_an_instance(self):
        """Prueba que el modelo puede crear una instancia."""
        instance = MyModel.objects.get(name="test")
        self.assertEqual(instance.name, "test")