from django.urls import path  # Import path for defining URL patterns
from . import views  # Import views from the current app

# Define URL patterns for the app
urlpatterns = [
    path('', views.home_view, name='home'),  # Home page
    path('contact/', views.contact_view, name='contact'),  # Contact form
    path('register/', views.register_view, name='register'),  # User registration
    path('login/', views.login_view, name='login'),  # User login
    path('logout/', views.logout_view, name='logout'),  # User logout
    path('profile/', views.profile_view, name='profile'),  # User profile (secured)
    path('article/create/', views.article_create_view, name='article_create'),  # Article creation
]
