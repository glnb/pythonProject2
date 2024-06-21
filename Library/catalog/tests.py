from django.test import TestCase
from .models import *
from datetime import datetime

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
    def test_string_representation(self):
        test_author = Author(name="Pablo")
        self.assertEqual(str(test_author), test_author.name)
        # str(genre) == genre.__str__()

    def test_author_creation(self):
        test_author = Author.objects.create(
            name="Pablo",
            date_birth="2024-06-23",
            date_death="2200-06-26")
        self.assertTrue(isinstance(test_author, Author))
        # Ne fonctione pas encore
        # self.assertLess(
        #     self,
        #     (datetime.strptime(test_author.date_birth, "%Y-%m-%d").timestamp()),
        #     (datetime.strptime(test_author.date_death, "%Y-%m-%d").timestamp()))
        self.assertEqual(test_author.__str__(), test_author.name)

class BookModelTest(TestCase):
    def






