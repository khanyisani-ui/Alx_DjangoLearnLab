1. Create Operation (create.md)
# create.md

## Command
```python
from bookshelf.models import Book

book = Book(title="1984", author="George Orwell", published_date="1949-06-08")
book.save()
print(book)

Expected Output
<Book: 1984>



### 2. Retrieve Operation (retrieve.md)
```markdown
# retrieve.md

## Command
```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)

Expected Output
1984 George Orwell 1949
python


### 3. Update Operation (update.md)
```markdown
# update.md

## Command
```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

Expected Output
Nineteen Eighty-Four
python


### 4. Delete Operation (delete.md)
```markdown
# delete.md

## Command
```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion by retrieving all books
books = Book.objects.all()
print(books)
Expected Output
bash

<Book: Nineteen Eighty-Four> # Before deletion
[]
python


### Comprehensive Documentation (CRUD_operations.md)
```markdown
# CRUD_operations.md

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