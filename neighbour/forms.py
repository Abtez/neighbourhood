from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import get_object_or_404

CHOICES = (
        ('Langata', 'Langata'),
        ('Dagoretti', 'Dagoretti'),
        ('Embakasi', 'Embakasi'),
        ('CBD', 'CBD'),
        ('Kasarani', 'Kasarani'),
        ('Kibra', 'Kibra'),
        ('Westland', 'Westland'),
        ('Parkland', 'Parkland'),
    )

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2') 
        
class NeighbourhoodForm(forms.ModelForm):
    neighbourhood_name = forms.ChoiceField(choices=CHOICES, required=True)
    
    class Meta:
        model = Neighbourhood
        fields = ('neighbourhood_name',) 
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'neighbourhood']
        
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'neighbourhood']
        
class EditHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ('neighbourhood_name',) 
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['profile', 'neighbourhood']

# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         exclude = ['project','profile']
        