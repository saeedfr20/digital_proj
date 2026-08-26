from django.test import TestCase
from .models import Category


class CategoryTest(TestCase):
    def test_category_creation(self):
        category = Category.objects.create(
            title='Python'
        )
        self.assertEqual(category.title, 'Python')
