from django.contrib.auth import login, authenticate
from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from django.http  import HttpResponse
import datetime as dt
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile/profile.html')

def business(request):
    return render(request, 'business.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        form_n = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid() and form_n.is_valid():
            neighb = form_n.save()               
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.neighbourhood = neighb            
            user.profile.bio = form.cleaned_data.get('bio')           
            user.profile.avatar = form.cleaned_data.get('avatar')           
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        return False
    return render(request, 'signup.html', {'form': SignUpForm, 'form_n': NeighbourhoodForm})

def signin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(request,'/')
    
    return render(request, 'registration/login.html')

@login_required
def logout(request):
    django_logout(request)
    return  HttpResponseRedirect('/')