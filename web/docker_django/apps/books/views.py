from django.shortcuts import render
from django.views.generic import ListView

from .models import Book, Writer

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'


class WriterListView(ListView):
    model = Writer
    template_name = 'books/writer_list.html'