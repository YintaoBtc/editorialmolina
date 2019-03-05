from django.shortcuts import render
from ..books.models import Book, Writer


def home(request):
    books=Book.objects.all()
    num_authors=Writer.objects.count()
    num_books=Book.objects.all().count()
    return render(request, "core/home.html", context={"books":books, "num_books":num_books, "num_authors":num_authors})

def about(request):
    return render(request, "core/about.html")

def store(request):
    return render(request, "core/store.html")

def blog(request):
    return render(request, "core/blog.html")

def contact(request):
    return render(request, "core/contact.html")