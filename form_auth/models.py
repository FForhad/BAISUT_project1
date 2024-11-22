from django.db import models  # Import Django's ORM for defining models

# Define the Article model to store blog articles in the database
class Article(models.Model):
    title = models.CharField(max_length=200)  # Field to store the title of the article
    content = models.TextField()  # Field to store the content of the article
    author = models.CharField(max_length=100)  # Field to store the name of the author

    def __str__(self):
        return self.title  # Return the article title as its string representation
