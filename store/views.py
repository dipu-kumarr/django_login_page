from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser  # Use User if not using a custom model
from .forms import UserRegisterForm, UserLoginForm
from django.urls import reverse

def say_hello(request):
    # product = Product.objects.get(id=1)
    return render(request, 'hello.html')
def home(request):
    return render(request, 'home.html')  # Ensure 'home.html' exists
    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')  # Change to your homepage URL name
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print(f"✅ Attempting to authenticate user: {username}")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                print("✅ Authentication successful for user:", user)
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('/admin/')  # Redirect to Django Admin Panel
            else:
                print("❌ Authentication failed")
                messages.error(request, "Invalid username or password.")
        else:
            print("❌ Form validation failed:", form.errors)
            messages.error(request, "Invalid login credentials.")

    else:
        form = UserLoginForm()

    return render(request, 'login.html', {'form': form})






@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('login')  # Redirect to login page after logout