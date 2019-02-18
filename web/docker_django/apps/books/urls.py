from django.urls import path

from .views import BookListView, WriterListView

urlpatterns= [
    path('', BookListView.as_view(), name = "books"),
    path('writer/', WriterListView.as_view(), name = "writer"),
]