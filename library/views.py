
from django.http import HttpResponse

def home(request):
    return HttpResponse("This is our bookshelf home page coming from views.")

def books(request):
    return HttpResponse("This is our bookshelf books page coming from views.")
