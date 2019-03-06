from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book, Writer

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'


class WriterListView(ListView):
    model = Writer
    template_name = 'books/writer_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'