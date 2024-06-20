from django.urls import path
from . import views
from . import views_books

urlpatterns = [
    path('', views.index, name='index'),
    path('books', views_books.index, name='books'),
]