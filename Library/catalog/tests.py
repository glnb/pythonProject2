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
    def setUp(self):
        self.author= Author.objects.create(name="Pablo")
        self.language = Language.objects.create(name="Spanish")
        self.book = Book.objects.create(
            author=self.author,
            language=self.language,
            title="",
            years="2024-03-30",
            isbn="1234567891011",
            summary="un test"
        )
        self.book.genre.set([Genre.objects.create(name="Aventure")])

    # Copier et coller en corrigeant certains point vu au-dessus
    def test_string_representation(self):
        self.assertEqual(str(self.book), self.book.title)

    def test_book_creation(self):
        self.assertTrue(isinstance(self.book, Book))
        self.assertEqual(self.book.__str__(), self.book.title)
        self.assertEqual(self.book.isbn, "1234567891011")







