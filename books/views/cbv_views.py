from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ..models import Book

class BookListView(ListView):
    """
    View to display a list of all books.
    """
    model = Book
    template_name = 'books/book_list.html'  # Specify your template name
    context_object_name = 'books'  # Use this name in the template to access the list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'This is CBVs'  # Additional context variable
        return context

class BookCreateView(CreateView):
    """
    View to add a new book to the list.
    """
    model = Book
    fields = ['title', 'author', 'published_date']  # Define fields to create
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')  # Redirect to the book list after adding

class BookUpdateView(UpdateView):
    """
    View to update an existing book.
    """
    model = Book
    fields = ['title', 'author', 'published_date']
    template_name = 'books/book_form.html'
    success_url = reverse_lazy('book_list')  # Redirect to the book list after updating

class BookDeleteView(DeleteView):
    """
    View to delete an existing book.
    """
    model = Book
    template_name = 'books/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')  # Redirect to the book list after deletion
