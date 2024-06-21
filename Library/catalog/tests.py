from django.test import TestCase
from .models import *

class GenreModelTest(TestCase):
    def test_string_representation(self):
        genre = Genre(name="Aventure")
        self.assertEqual(str(genre), genre.name)
        # str(genre) == genre.__str__()

    def test_genre_creation(self):
        test_genre = Genre.objects.create(name="Aventure")
        self.assertTrue(isinstance(test_genre, Genre))
        self.assertEqual(test_genre.name, "Aventure")

    def test_genre_unique(self): #Doit être vrai
        num_genre = Genre.objects.filter(name="Aventure").count()
        self.assertNotEqual(num_genre, 2)


class AuthorModelTest(TestCase):