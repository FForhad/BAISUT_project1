from django.db import models
from django.utils import timezone

# Model Example with Field Types, Field Options, and PK/AutoField
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)                # Auto-incremented ID as primary key
    name = models.CharField(max_length=100, unique=True)           # CharField with unique constraint
    description = models.TextField(blank=True, default="No description available") # TextField with default
    price = models.DecimalField(max_digits=10, decimal_places=2)   # Decimal field for price
    quantity = models.IntegerField()                               # IntegerField for quantity
    available = models.BooleanField(default=True)                  # BooleanField for stock status


    class Meta:
        ordering = ['price']                       # Meta option: default ordering by price
        verbose_name = "Product Item"              # Meta option: singular name
        verbose_name_plural = "Product Items"      # Meta option: plural name
        unique_together = ['name', 'price']        # Unique constraint on name-price pairs

    def __str__(self):
        return self.name

# Relations Between Models
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Publication(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # ForeignKey for Many-to-One relation
    published_date = models.DateField()

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)                          # Many-to-Many relation with Publication

    def __str__(self):
        return self.name

class Biography(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE) # One-to-One relation with Author
    content = models.TextField()

    def __str__(self):
        return f"Biography of {self.author.name}"

# Model with Custom Method
class Event(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def duration(self):
        return self.end_date - self.start_date  # Returns event duration as timedelta

    @classmethod
    def upcoming_events(cls):
        return cls.objects.filter(start_date__gte=timezone.now())  # Class method for filtering upcoming events

# # Example Queries
# # Get all books
# books = Book.objects.all()

# # Filter books by author name
# books_by_author = Book.objects.filter(author__name="John Doe")

# # Get a single book (raises error if not found)
# specific_book = Book.objects.get(id=1)

# # Count total number of books
# book_count = Book.objects.count()

# # Get recent books published in the last year
# recent_books = Book.objects.filter(published_date__gte=timezone.now() - timezone.timedelta(days=365))
