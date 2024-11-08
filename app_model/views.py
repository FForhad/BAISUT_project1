# views.py

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Publication, Author, Event

# View to list all publications
def list_publications(request):
    publications = Publication.objects.all()
    return render(request, 'models/publication_list.html', {'publications': publications})

# View to filter publications by author name
def publications_by_author(request, author_name):
    publications = Publication.objects.filter(author__name=author_name)
    return render(request, 'models/publications_by_author.html', {'publications': publications, 'author_name': author_name})

# View to get a specific publication by ID
def specific_publication(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    return render(request, 'models/publication_detail.html', {'publication': publication})

# View to get count of all publications
def publication_count(request):
    count = Publication.objects.count()
    return render(request, 'models/publication_count.html', {'count': count})

# View to get publications published within the last year
def recent_publications(request):
    recent_publications = Publication.objects.filter(
        published_date__gte=timezone.now() - timezone.timedelta(days=365)
    )
    return render(request, 'models/recent_publications.html', {'publications': recent_publications})

# View to get upcoming events
def upcoming_events(request):
    events = Event.objects.upcoming_events()
    return render(request, 'models/upcoming_events.html', {'events': events})
