# api/test_views.py
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book

class BookAPITests(APITestCase):
    
    def setUp(self):
        # Create a test user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.book_data = {
            "title": "Test Book",
            "author": "Test Author",
            "publication_year": 2024,
        }
        self.book = Book.objects.create(**self.book_data)

    def test_create_book_authenticated(self):
        """Test creating a book with authentication"""
        url = '/api/books/'
        self.client.login(username='testuser', password='testpassword')  # Authenticate user
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], self.book_data['title'])

    def test_create_book_unauthenticated(self):
        """Test creating a book without authentication"""
        url = '/api/books/'
        response = self.client.post(url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_read_book(self):
        """Test retrieving a single book by ID"""
        url = f'/api/books/{self.book.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book.title)

    def test_update_book_authenticated(self):
        """Test updating a book with authentication"""
        url = f'/api/books/{self.book.id}/'
        update_data = {"title": "Updated Book"}
        self.client.login(username='testuser', password='testpassword')  # Authenticate user
        response = self.client.put(url, update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], update_data['title'])

    def test_delete_book_authenticated(self):
        """Test deleting a book with authentication"""
        url = f'/api/books/{self.book.id}/'
        self.client.login(username='testuser', password='testpassword')  # Authenticate user
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_book_filtering(self):
        """Test filtering books by title"""
        Book.objects.create(title="Another Book", author="Another Author", publication_year=2022)
        url = '/api/books/?title=Test Book'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Book")

    def test_book_search(self):
        """Test searching books by author"""
        Book.objects.create(title="Searchable Book", author="Search Author", publication_year=2023)
        url = '/api/books/?search=Search Author'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], "Search Author")

    def test_book_ordering(self):
        """Test ordering books by publication year"""
        Book.objects.create(title="Old Book", author="Old Author", publication_year=2000)
        url = '/api/books/?ordering=publication_year'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2000)
