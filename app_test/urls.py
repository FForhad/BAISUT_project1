# urls.py
from django.urls import path
from .views import BookListView, BookDetailView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),               # URL for listing all books
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),  # URL for book details
]

from .views import book_list, book_detail

urlpatterns = [
    path('books/', book_list, name='book_list'),                # URL for listing all books
    path('books/<int:pk>/', book_detail, name='book_detail'),   # URL for book details
]