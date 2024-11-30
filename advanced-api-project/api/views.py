# api/views.py

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class BookListView(generics.ListCreateAPIView):
    """
    get:
    Return a list of all the existing books.

    post:
    Create a new book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    get:
    Retrieve a book instance.

    put:
    Update a book instance.

    delete:
    Delete a book instance.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
