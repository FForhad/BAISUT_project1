from django.urls import path

#FBVs
from .views.fbv_views import book_list, book_add, book_update, book_delete

#CBVs
from .views.cbv_views import BookListView, BookCreateView, BookUpdateView, BookDeleteView


urlpatterns = [
    #FBVs
    path('fbv/', book_list, name='book_list'),          # URL for viewing the book list
    path('fbv/add/', book_add, name='book_add'),         # URL for adding a new book
    path('fbv/update/<int:pk>/', book_update, name='book_update'),  # URL for updating a book
    path('fbv/delete/<int:pk>/', book_delete, name='book_delete'),  # URL for deleting a book

    #CBVs
    path('cbv/', BookListView.as_view(), name='book_list'),  # URL for viewing the book list
    path('cbv/add/', BookCreateView.as_view(), name='book_add'),  # URL for adding a new book
    path('cbv/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),  # URL for updating a book
    path('cbv/delete/<int:pk>/', BookDeleteView.as_view(), name='book_delete'),  # URL for deleting a book
]


