from django.contrib import admin
from .models import Product, Author, Publication, Library, Biography, Event

# Custom admin for Product model
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'available')
    list_filter = ('available', 'price')
    search_fields = ('name', 'description')
    ordering = ('price',)

# Custom admin for Author model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Custom admin for Publication model
@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    list_filter = ('author', 'published_date')
    search_fields = ('title', 'author__name')
    date_hierarchy = 'published_date'

# Custom admin for Library model
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    filter_horizontal = ('publications',)  # Allows easier management of Many-to-Many relationships

# Custom admin for Biography model
@admin.register(Biography)
class BiographyAdmin(admin.ModelAdmin):
    list_display = ('author',)
    search_fields = ('author__name',)

# Custom admin for Event model
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'duration')
    list_filter = ('start_date', 'end_date')
    search_fields = ('name',)
    date_hierarchy = 'start_date'

    # Method to display the duration in the list display
    def duration(self, obj):
        return obj.duration()
    duration.short_description = 'Event Duration'
