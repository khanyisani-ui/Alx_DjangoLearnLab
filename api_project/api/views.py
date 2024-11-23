from django.shortcuts import render

from rest_framework import generics
from .models import Book, MyModel
from .serializers import BookSerializer, MyModelSerializer

class BookListCreateAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
    

