# *coding: utf-8*

from django.test import TestCase
from models import Category


class CategoryTests(TestCase):
    @classmethod  # <- setUpClass doit être une méthode de classe, attention !
    def setUpTestData(cls):
        Category.objects.create(name="Bars")

    def test_bars(self):
        """
        Vérifie si la categorie de type Bars existe bien
        """
        self.assertTrue(
            Category.objects.filter(name='Bars').exists()
        )
