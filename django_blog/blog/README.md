Testing the Authentication System
To test the authentication system:

Register a new user by visiting /register/.
Log in using the created credentials at /login/.
Log out using the /logout/ path.
Edit your profile by visiting /profile/.

# Django Blog Project

## Blog Post Management Features

This project allows users to create, read, update, and delete (CRUD) blog posts. Below are the steps to set up and use the blog post management features.

### Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/django_blog.git
    cd django_blog
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Apply Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

### Usage

1. **Access the Blog**:
    Open your browser and go to `http://127.0.0.1:8000/`.

2. **Create a New Post**:
    - Go to `/post/new/` to create a new blog post.
    - Only authenticated users can create new posts.

3. **View Posts**:
    - Go to `/` to view the list of all blog posts.
    - Click on a post title to view the details of the post.

4. **Edit a Post**:
    - Go to `/post/<int:pk>/edit/` to edit a post.
    - Only the author of the post can edit it.

5. **Delete a Post**:
    - Go to `/post/<int:pk>/delete/` to delete a post.
    - Only the author of the post can delete it.

### Permissions

- **Authenticated Users**:
  - Can create new posts.
  - Can edit or delete their own posts.

- **Unauthenticated Users**:
  - Can view the list of posts and post details.

### Additional Notes

- Ensure that CSRF tokens are included in all forms for security.
- Passwords are securely handled using Django’s built-in hashing algorithms.

For further details, refer to the code comments and docstrings in the project files.

