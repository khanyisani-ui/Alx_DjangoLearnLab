### 2. Retrieve Operation

## Command
```python
from bookshelf.models import Book

book = Book.objects.get(title="1984")
print(book.title, book.author, book.published_date)

Expected Output
1984 George Orwell 1949