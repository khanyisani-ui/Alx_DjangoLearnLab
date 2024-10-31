from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # Define the fields to display in the list view
    list_display = ('title', 'author', 'publication_year')
    
    # Add search functionality
    search_fields = ('title', 'author')
    
    # Add list filters
    list_filter = ('author', 'publication_year')

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
