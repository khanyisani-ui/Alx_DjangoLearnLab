# views.py
from rest_framework import generics 
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Customize the CreateView to handle submission and additional validation
class BookCreateView(generics.CreateAPIView):
    """
    Create a new book. This endpoint is restricted to authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create a book
    
    def perform_create(self, serializer):
        """
        Perform custom logic during the creation process (e.g., set the owner to the current user).
        """
        serializer.save(owner=self.request.user)
    
    def perform_create(self, serializer):
        # Optionally add custom logic before creating the book (e.g., setting user)
        serializer.save(owner=self.request.user)

# Customize the UpdateView to ensure validation and proper updating
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update a book
    
    def perform_update(self, serializer):
        # Optionally add custom logic before updating the book (e.g., checking ownership)
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete a book
