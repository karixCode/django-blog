from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import Post, Comment, User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'avatar', 'bio']

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'name', 'bio', 'password1', 'password2']


class ChangeUserInfoForm(forms.ModelForm):
   class Meta:
       model = User
       fields = ['avatar', 'username', 'name', 'bio']