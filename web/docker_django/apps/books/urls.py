from django.urls import path

from .views import BookListView, WriterListView, BookDetailView

urlpatterns= [
    path('', BookListView.as_view(), name = "books"),
    path('writer/', WriterListView.as_view(), name = "writer"),
    path('<int:pk>/', BookDetailView.as_view(), name="book"),
]