from django.shortcuts import render
from .models import Book

# Create your views here.
def home(request):
    return render(request, 'shelf/home.html')

def books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'shelf/books.html', context)

def book_add(request):
    return render(request, 'shelf/book_add.html')

def book_detail(request, pk):
    
    context = {
        'book_id': pk
    }
    return render(request, 'shelf/book_detail.html', context)  

def book_edit(request, pk):
    context = {
        'book_id': pk
    }
    return render(request, 'shelf/book_edit.html', context)

def book_delete(request, pk):
    context = {
        'book_id': pk
    }
    return render(request, 'shelf/book_delete.html', context)

