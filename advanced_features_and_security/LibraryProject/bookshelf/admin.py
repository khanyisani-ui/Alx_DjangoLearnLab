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


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'date_of_birth', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('email', 'username', 'date_of_birth', 'is_staff')
    search_fields = ('email', 'username')

admin.site.register(CustomUser, CustomUserAdmin)

#Groups with assigned permissions
from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import CustomUser, Article

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Article)

# Create groups and assign permissions programmatically
def create_groups_and_permissions():
    content_type = ContentType.objects.get_for_model(Article)

    permissions = {
        'can_view': Permission.objects.get(codename='can_view', content_type=content_type),
        'can_create': Permission.objects.get(codename='can_create', content_type=content_type),
        'can_edit': Permission.objects.get(codename='can_edit', content_type=content_type),
        'can_delete': Permission.objects.get(codename='can_delete', content_type=content_type),
    }

    groups = {
        'Viewers': ['can_view'],
        'Editors': ['can_view', 'can_create', 'can_edit'],
        'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
    }

    for group_name, perms in groups.items():
        group, created = Group.objects.get_or_create(name=group_name)
        for perm in perms:
            group.permissions.add(permissions[perm])

create_groups_and_permissions()



