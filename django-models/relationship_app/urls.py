from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import list_books

urlpatterns = [
    # URL for listing books
    path('books/', views.list_books, name='list_books'),

    # URL for displaying details of a specific library
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]


from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
]


# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('books/add/', views.add_book, name='add_book'),
    path('books/edit/<int:pk>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:pk>/', views.delete_book, name='delete_book'),
    # other urls...
]

