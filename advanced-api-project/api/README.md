# Advanced API Project

## View Configurations

### Book List View

- URL: `/books/`
- Methods: `GET`, `POST`
- Permissions: Read-only for unauthenticated users; authenticated users can create new books.

### Book Detail View

- URL: `/books/<int:pk>/`
- Methods: `GET`, `PUT`, `DELETE`
- Permissions: Read-only for unauthenticated users; authenticated users can update or delete books.

### Customizations

- Permissions: Using `IsAuthenticatedOrReadOnly` to allow read access to all users and write access to authenticated users.
- Serializers: `BookSerializer` used for data serialization and validation.




## Unit Testing the Book API Endpoints

### Test Cases
1. **Create Book (Authenticated)**: Verifies that a book can be created by an authenticated user.
2. **Create Book (Unauthenticated)**: Verifies that a book cannot be created without authentication.
3. **Read Book**: Verifies that a book can be retrieved by its ID.
4. **Update Book (Authenticated)**: Verifies that a book can be updated by an authenticated user.
5. **Delete Book (Authenticated)**: Verifies that a book can be deleted by an authenticated user.
6. **Filter Books**: Verifies that books can be filtered by their title.
7. **Search Books**: Verifies that books can be searched by author.
8. **Order Books**: Verifies that books can be ordered by publication year.

### Running the Tests
To run the tests, use the following command:
```bash
python manage.py test api

