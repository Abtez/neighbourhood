from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    city = forms.CharField(max_length=200, required=True)
    location = forms.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ('city','location','username', 'first_name', 'last_name', 'email', 'password1', 'password2') 
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'profile', 'like', 'screenshots']

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         exclude = ['project','profile']
        