from django.db import models

class Author(models.Model):
    """
    Author Model:
    Represents an author who can have multiple books.
    
    Fields:
    - name: The name of the author.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book Model:
    Represents a book written by an author.
    
    Fields:
    - title: The title of the book.
    - publication_year: The year the book was published.
    - author: ForeignKey linking to the Author model, establishing a one-to-many relationship.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
