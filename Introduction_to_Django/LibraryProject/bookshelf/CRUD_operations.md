## Create Operation
### Command
```python
from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", published_date="1949-06-08")
book.save()
print(book)
Output
<Book: 1984>

# Retrieve Operation
from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
Output
1984 George Orwell 1949

# Update Operation
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
Output
Nineteen Eighty-Four

# Delete Operation
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by retrieving all books
books = Book.objects.all()
print(books)
Output
<Book: Nineteen Eighty-Four> # Before deletion
[]