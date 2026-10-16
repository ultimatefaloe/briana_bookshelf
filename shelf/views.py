from django.shortcuts import redirect, render
from .models import Book
from .forms import BookForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST


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


@login_required()
def book_add(request):
    context = {}
    
    if request.method == 'POST':
        form = BookForm(request.POST)
        files = request.FILES.get('book_cover')
        if form.is_valid():
            book = form.save(commit=False)
            book.owner = request.user
            if files:
                book.book_cover = files
            book.save()
            messages.success(request, 'Book added successfully!')
            return redirect('shelf:books')
        else:
            messages.error(request, 'Error adding book. Please check the form for errors.')
    else:
        form = BookForm()
    
    context['form'] = form
    return render(request, 'shelf/book_add.html', context)

def book_detail(request, pk):
    context = {}
    try:
        book = Book.objects.get(pk=pk)
        context['book'] = book
    except Book.DoesNotExist:
        messages.error(request, 'Book not found.')
        return redirect('shelf:books')
    
    return render(request, 'shelf/book_detail.html', context)  

@login_required()
def book_edit(request, pk):
    context = {}
    if not pk:
        messages.error(request, 'Book ID is required for editing.')
        return redirect('shelf:books')
    
    # get book by id
    try:
        book = Book.objects.get(pk=pk)
        print(book.book_cover)
    except Book.DoesNotExist:
        messages.error(request, 'Book not found.')
        return redirect('shelf:books')
    
    # check for authorization
    if request.user != book.owner:
        messages.error(request, 'You do not have permission to edit this book.')
        return redirect('shelf:books')
    
    # handle form submission
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        files = request.FILES.get('book_cover')
        if form.is_valid():
            book = form.save(commit=False)
            if files:
                book.book_cover = files
            book.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('shelf:books')
        else:
            messages.error(request, 'Error updating book. Please check the form for errors.')
        
    else:
        context['form'] = BookForm(instance=book)
    return render(request, 'shelf/book_edit.html', context)

@login_required()
def book_delete(request, pk):
    # check if book id is provided
    if not pk:
        messages.error(request, 'Book ID is required for deletion.')
        return redirect('shelf:books')
    
    # get book by id
    try:
        book = Book.objects.get(pk=pk)
        print(book.book_cover)
    except Book.DoesNotExist:
        messages.error(request, 'Book not found.')
        return redirect('shelf:books')
    
    # check for autorization
    if request.user != book.owner:
        messages.error(request, 'You do not have permission to delete this book.')
        return redirect('shelf:books')
        

    # hanle deletion
    if request.method == 'POST':
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            messages.success(request, 'Book deleted successfully!')
            return redirect('shelf:books')
            
        except Book.DoesNotExist:
            messages.error(request, 'Book not found.')
            return redirect('shelf:books')
    else:
        messages.error(request, 'Invalid request method for deletion.')
        return redirect('shelf:books')