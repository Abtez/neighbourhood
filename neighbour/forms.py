from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import get_object_or_404

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2') 
        
class NeighbourhoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        exclude = ['admin', 'CHOICES', 'location', 'population']
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'neighbourhood']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile', 'neighbourhood']

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         exclude = ['project','profile']
        