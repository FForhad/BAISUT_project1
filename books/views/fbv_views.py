from django.shortcuts import render, redirect, get_object_or_404
from ..models import Book

def book_list(request):
    """
    View to display a list of all books.
    """
    books = Book.objects.all()  # Retrieves all books from the database
    context = {
        'books': books,
        'message': 'This is FBVs'  # Additional context variable
    }
    return render(request, 'books/book_list.html', context)

def book_add(request):
    """
    View to add a new book to the list.
    """
    if request.method == 'POST':
        # Example code for creating a book instance; form logic will be added here.
        new_book = Book.objects.create(
            title=request.POST.get('title'),
            author=request.POST.get('author'),
            published_date=request.POST.get('published_date')
        )
        return redirect('book_list')  # Redirects to the book list after adding a book
    return render(request, 'books/book_form.html')  # Renders the form for adding a book

def book_update(request, pk):
    """
    View to update an existing book.
    """
    book = get_object_or_404(Book, pk=pk)  # Retrieves the book by primary key
    if request.method == 'POST':
        # Updates the book's fields with new values from the form
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.save()  # Saves the updated book to the database
        return redirect('book_list')  # Redirects to the book list after updating
    return render(request, 'books/book_form.html', {'book': book})  # Renders the form for editing

def book_delete(request, pk):
    """
    View to delete an existing book.
    """
    book = get_object_or_404(Book, pk=pk)  # Retrieves the book by primary key
    if request.method == 'POST':
        book.delete()  # Deletes the book from the database
        return redirect('book_list')  # Redirects to the book list after deletion
    return render(request, 'books/book_confirm_delete.html', {'book': book})  # Renders a delete confirmation page
