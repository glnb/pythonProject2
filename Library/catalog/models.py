import uuid

from django.db import models

class Genre(models.Model):
    """ Genre, ex : romance, FX , ... """
    name = models.CharField(
        max_length=200,
        help_text="Genre(s) du livre",
        unique=True,
    )

    def __str__(self):
        return self.name

class Language(models.Model):
    """ Langue, ex : Anglais, Français , ... """
    name = models.CharField(
        max_length=100,
        help_text="La langue d'origine du livre",
        unique=True,
    )

    def __str__(self):
        return self.name

class Author(models.Model):
    """ Autheur, ex : JK R. ... """
    name = models.CharField(max_length=200)
    date_birth = models.DateField(null=True, blank=True)
    date_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    """ Le Livre ..."""
    title = models.CharField(max_length=200)
    summary = models.TextField(
        max_length=1000,
        help_text="Ex: Résumé du livre",
    )
    years = models.DateField(null=False, blank=False)
    isbn = models.CharField(
        max_length=13,
        unique=True,
        help_text="ISBN de 13 caractères",
    )
    author = models.ForeignKey(
        Author,
        null=True,
        on_delete=models.RESTRICT,
    )
    language = models.ForeignKey(
        Language,
        on_delete=models.SET_NULL,
        null=True,
    )
    genre = models.ManyToManyField(
        Genre, help_text="Sélectionnez le genre du livre"
    )

class State(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Numéros unique du livre dans la librairie"
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.RESTRICT,
        null=True
    )
    date_emprunt = models.DateField(null=False)
    date_retour = models.DateField(null=True, blank=True)
    VAR_STATUS = (
        ('m', 'Maintenance'),
        ('d', 'Disponible'),
        ('r', 'Réservé'),
    )
    status = models.CharField(
        max_length=1,
        blank=True,
        default='d',
        help_text="Status du livre ?",
        choices=VAR_STATUS
    )