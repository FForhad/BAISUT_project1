from django.db import models

# Defining a simple model for a "Blog Post"
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

#Basic Fiels Types
class Product(models.Model):
    name = models.CharField(max_length=100)         # CharField for short text
    description = models.TextField()                # TextField for longer text
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Decimal for currency
    quantity = models.IntegerField()                # Integer for whole numbers
    available = models.BooleanField(default=True)   # Boolean for true/false

    def __str__(self):
        return f"{self.name} - ${self.price}"

#Field Options
class UserProfile(models.Model):
    username = models.CharField(max_length=50, unique=True)   # unique ensures no duplicate usernames
    email = models.EmailField(null=True, blank=True)          # null=True allows NULL in database; blank=True allows form submissions without a value
    bio = models.TextField(default="No bio available")        # default provides a default text
    status = models.CharField(
        max_length=10,
        choices=[("ACTIVE", "Active"), ("INACTIVE", "Inactive")],
        default="ACTIVE"
    )   # choices limits values

    def __str__(self):
        return self.username

#PK and AutoField
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)     # Auto-incremented ID
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.CharField(max_length=20, primary_key=True)   # Custom primary key
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} by {self.customer.name}"


#Relation between models.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)   # Many-to-One
    published_date = models.DateField()

    def __str__(self):
        return self.title

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)   # Many-to-Many

    def __str__(self):
        return self.name

class Biography(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE)  # One-to-One
    content = models.TextField()

    def __str__(self):
        return f"Biography of {self.author.name}"

#MetaOptions
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ['price']                        # Default order by price
        verbose_name = "Product Item"               # Customized singular name
        verbose_name_plural = "Product Items"       # Customized plural name
        unique_together = ['name', 'price']         # Ensures name-price pairs are unique

    def __str__(self):
        return self.name


#Model Methods
class Event(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name

    def duration(self):
        return self.end_date - self.start_date      # Returns timedelta for event duration

    @classmethod
    def upcoming_events(cls):
        return cls.objects.filter(start_date__gte=timezone.now())  # Class method to filter events
    

#Query
from django.utils import timezone

# Get all books
books = Book.objects.all()

# Filter books by author name
books_by_author = Book.objects.filter(author__name="John Doe")

# Get a single book (raises error if not found)
specific_book = Book.objects.get(id=1)

# Aggregation: Count the number of books
book_count = Book.objects.count()

# Get books published after a certain date
recent_books = Book.objects.filter(published_date__gte=timezone.now() - timezone.timedelta(days=365))

# Chaining filters: Get books by a specific author published in the last year
recent_books_by_author = Book.objects.filter(
    author__name="John Doe",
    published_date__gte=timezone.now() - timezone.timedelta(days=365)
)
