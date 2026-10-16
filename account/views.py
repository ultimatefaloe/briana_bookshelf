from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_http_methods

# Create your views here.
def login_view(request):
    context = {}

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')

            next_url = request.POST.get('next') or request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(
                next_url, allowed_hosts={request.get_host()}, require_https=request.is_secure()
            ):
                return redirect(next_url)
            return redirect('shelf:home')
        else:
            print(form.errors)
            messages.error(request, 'Invalid login credentials. Please try again.')
            context['form'] = form
    else:
        form = LoginForm()
        context['form'] = form

    return render(request, 'account/login.html', context)

def register_view(request):
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('shelf:home')
        else:
            print(form.errors)
            messages.error(request, 'Invalid registration credentials. Please try again.')
            context['form'] = form
    else:
        form = RegisterForm()
        context['form'] = form

    return render(request, 'account/register.html', context)

@require_http_methods(["POST"])
def logout_view(request):
    
    if request.method == 'POST':
        logout(request)
        messages.success(request, 'You have been logged out.')
        return redirect('account:login')
    
    return redirect("shelf:home")
  
def profile_view(request):
    return HttpResponse("Profile Page")

def profile_edit_view(request):
    return HttpResponse("Profile Edit Page")