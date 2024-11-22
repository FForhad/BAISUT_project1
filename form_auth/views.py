from django.shortcuts import render, redirect  # Import render for templates and redirect for navigation
from django.contrib.auth import authenticate, login, logout  # Import auth methods
from django.contrib.auth.decorators import login_required  # Import decorator for secured views
from .forms import ContactForm, RegistrationForm, ArticleForm  # Import forms defined in forms.py
from .models import Article  # Import the Article model

# Home page view
def home_view(request):
    return render(request, 'form_auth/home.html')  # Render the home.html template

# Contact form view
def contact_view(request):
    if request.method == 'POST':  # Check if the request is a POST (form submission)
        form = ContactForm(request.POST)  # Instantiate the form with submitted data
        if form.is_valid():  # Check if the form data is valid
            print(form.cleaned_data)  # Print cleaned data for debugging
    else:
        form = ContactForm()  # Create an empty form instance for GET requests
    return render(request, 'form_auth/contact.html', {'form': form})  # Render the contact page with the form

# User registration view
def register_view(request):
    if request.method == 'POST':  # Check if the request is a POST
        form = RegistrationForm(request.POST)  # Instantiate the form with submitted data
        if form.is_valid():  # Validate the form
            form.save(commit=False)  # Save the form without committing to the database yet
            user = form.save()  # Save the user object
            user.set_password(form.cleaned_data['password'])  # Hash the user's password
            user.save()  # Save the hashed password to the database
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()  # Create an empty form for GET requests
    return render(request, 'form_auth/register.html', {'form': form})  # Render the register page with the form

# User login view
def login_view(request):
    if request.method == 'POST':  # Check if the request is a POST
        username = request.POST['username']  # Get the submitted username
        password = request.POST['password']  # Get the submitted password
        user = authenticate(request, username=username, password=password)  # Authenticate the user
        if user:  # If the user exists and credentials are correct
            login(request, user)  # Log the user in
            return redirect('profile')  # Redirect to the profile page
        else:
            return render(request, 'form_auth/login.html', {'error': 'Invalid credentials'})  # Show an error message
    return render(request, 'form_auth/login.html')  # Render the login page for GET requests

# User logout view
def logout_view(request):
    logout(request)  # Log the user out
    return redirect('login')  # Redirect to the login page

# Secured profile page view
@login_required  # Ensure the user is logged in to access this view
def profile_view(request):
    return render(request, 'form_auth/profile.html')  # Render the profile page

# Article creation view
@login_required  # Ensure the user is logged in to access this view
def article_create_view(request):
    if request.method == 'POST':  # Check if the request is a POST
        form = ArticleForm(request.POST)  # Instantiate the form with submitted data
        if form.is_valid():  # Validate the form
            form.save()  # Save the article to the database
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = ArticleForm()  # Create an empty form for GET requests
    return render(request, 'form_auth/article_form.html', {'form': form})  # Render the article creation page
