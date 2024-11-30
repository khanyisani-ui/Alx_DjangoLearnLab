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
