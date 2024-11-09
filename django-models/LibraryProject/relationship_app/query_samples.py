# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Get all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# Query 2: List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

# Query 3: Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

# Example usage:
if __name__ == "__main__":
    # Example Query 1: Get all books by a specific author
    books_by_author = get_books_by_author('J.K. Rowling')
    print(f"Books by J.K. Rowling:")
    for book in books_by_author:
        print(f"- {book.title}")

    # Example Query 2: List all books in a library
    books_in_library = get_books_in_library('Central Library')
    print(f"\nBooks in Central Library:")
    for book in books_in_library:
        print(f"- {book.title}")

    # Example Query 3: Retrieve the librarian for a library
    librarian = get_librarian_for_library('Central Library')
    print(f"\nLibrarian for Central Library: {librarian.name}")
