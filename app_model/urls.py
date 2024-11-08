# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('publications/', views.list_publications, name='list_publications'),
    path('publications/author/<str:author_name>/', views.publications_by_author, name='publications_by_author'),
    path('publication/<int:publication_id>/', views.specific_publication, name='specific_publication'),
    path('publications/count/', views.publication_count, name='publication_count'),
    path('publications/recent/', views.recent_publications, name='recent_publications'),
    path('events/upcoming/', views.upcoming_events, name='upcoming_events'),
]
