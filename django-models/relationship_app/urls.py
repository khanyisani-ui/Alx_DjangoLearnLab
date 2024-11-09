from django.urls import path
from . import views

urlpatterns = [
    # URL for listing books
    path('books/', views.list_books, name='list_books'),

    # URL for displaying details of a specific library
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
