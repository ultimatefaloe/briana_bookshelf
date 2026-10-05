from django.shortcuts import redirect, render
from .models import Book
from .forms import BookForm
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'shelf/home.html')

def books(request):
    filter = {
        'search': request.GET.get('search', ''),
        'status': request.GET.get('status', '')
    }
    
    if filter['search'] and filter['status']:
        books = Book.objects.filter(title__icontains=filter['search'], status=filter['status'])
    elif filter['search']:
        books = Book.objects.filter(title__icontains=filter['search'])
    elif filter['status']:
        books = Book.objects.filter(status=filter['status'])
    else:
        books = Book.objects.all()

    statuses = Book.STATUS_CHOICES
    context = {
        'books': books,
        'statuses': statuses,
        'filter': filter
    }
    return render(request, 'shelf/books.html', context)

def book_add(request):
    context = {}
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('shelf:books')
        else:
            messages.error(request, 'Error adding book. Please check the form for errors.')
    else:
        form = BookForm()
    
    context['form'] = form
    return render(request, 'shelf/book_add.html', context)

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

