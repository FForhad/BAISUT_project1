from django import forms  # Import Django's forms module for handling forms
from django.contrib.auth.models import User  # Import the default User model for authentication
from .models import Article  # Import the Article model from the app

# Define a basic contact form for user input
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")  # Input field for name
    email = forms.EmailField(label="Your Email")  # Input field for email
    message = forms.CharField(widget=forms.Textarea, label="Your Message")  # Textarea for messages

# Define a user registration form
class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Input field for password (masked)
    confirm_password = forms.CharField(widget=forms.PasswordInput)  # Field to confirm password

    class Meta:
        model = User  # Associate this form with the User model
        fields = ['username', 'email', 'password']  # Include these fields in the form

    def clean(self):
        # Overriding the clean method for custom validation
        cleaned_data = super().clean()  # Call the parent class's clean method
        if cleaned_data.get('password') != cleaned_data.get('confirm_password'):  # Check if passwords match
            raise forms.ValidationError("Passwords do not match!")  # Raise an error if mismatched
        return cleaned_data  # Return cleaned data

# Define a model-based form for creating or editing articles
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article  # Associate the form with the Article model
        fields = ['title', 'content', 'author']  # Include these fields in the form
