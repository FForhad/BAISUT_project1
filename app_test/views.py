#CBVs
# views.py
from django.views.generic import ListView, DetailView
#generic [ListView, DetailView, CreateView, UpdateView, DeleteView]
from .models import Book

# View to list all books
class BookListView(ListView):
    model = Book                        # The model we're displaying
    template_name = 'book_list.html'    # The template to render
    context_object_name = 'books'       # Name of the variable to use in the template

# View to show details for a single book
class BookDetailView(DetailView):
    model = Book                        # The model to use
    template_name = 'book_detail.html'  # The template to render
    context_object_name = 'book'        # Name of the variable to use in the template


####################################
#FBVs

# views.py
from django.shortcuts import render, get_object_or_404
from .models import Book

# Function-based view to list all books
def book_list(request):
    books = Book.objects.all()  # Get all books from the database
    return render(request, 'book_list.html', {'books': books})  # Pass the books to the template

# Function-based view to show details for a single book
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)  # Get a book by primary key or return 404 if not found
    return render(request, 'book_detail.html', {'book': book})  # Pass the book to the template
