from datetime import datetime

from django.shortcuts import render
from .models import Book,Author,State


def index(request):
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_book_reserved = State.objects.filter(status="r").count()
    return render(request,
                  'catalog/books.html',
                  context={
                      'num_books':num_books,
                      'num_authors':num_authors,
                      'num_book_reserved':num_book_reserved,
                           },
                  )
