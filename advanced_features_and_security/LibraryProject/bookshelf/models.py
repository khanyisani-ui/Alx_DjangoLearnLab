from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField (max_length = 200)
    author = models.CharField (max_length = 100)
    publication_year = models.IntegerField ()
    
    
# Custom User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, date_of_birth=date_of_birth, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, date_of_birth, password, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

# Updating Foreignkeys
from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField()

    def __str__(self):
        return self.user.username
    
    
#Custom permissions
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_view", "Can view articles"),
            ("can_create", "Can create articles"),
            ("can_edit", "Can edit articles"),
            ("can_delete", "Can delete articles"),
        ]

    def __str__(self):
        return self.title


