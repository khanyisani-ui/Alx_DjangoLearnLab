from django import forms
from django.contrib.auth.models import User
from .models import Post
from .models import Comment

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        
        
# Post Form
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        
# Comment Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
