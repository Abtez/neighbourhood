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
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist


@login_required
def home(request):
    return render(request, 'home.html')

def view_by_category(request,category):
    try:
        post = Post.filter_by_category(category)
        message = category
    except ObjectDoesNotExist:
        raise Http404()
    return render(request, 'location.html',{"post": post, 'message':category})

@login_required
def index(request, name):    
    hood = get_object_or_404(Name, neighbourhood_name__icontains=name)
    post = Post.objects.filter(neighbour=hood).order_by('-date')
    
    return render(request, 'index.html', {'post':post})

@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    form = EditProfileForm(instance=profile)
    form_ = EditHoodForm(instance=profile.neighbourhood.hood_name)
    post_count = Post.objects.filter(profile=profile).count()
    
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = user
            data.neighbourhoob = profile.neighbourhood 
            data.save()
            return HttpResponseRedirect(reverse('profile', args=[username]))
        else:
            form = EditProfileForm(instance=profile)
            
    if request.method == "POST":
        form_n = EditHoodForm(request.POST, instance=profile.neighbourhood.hood_name)
        if form_n.is_valid():
            data = form_n.save()
            data.save()
            return HttpResponseRedirect(reverse('profile', args=[username]))
        else:
            form_n = EditHoodForm(instance=profile.neighbourhood.hood_name)
        
    return render(request, 'profile/profile.html', {'profile':profile, 'post_count':post_count, 
                                                    'form':EditProfileForm, 'form_n':EditHoodForm})

@login_required
def business(request):
    hood_user = request.user
    user = hood_user.profile.neighbourhood.pk
    hood = get_object_or_404(Neighbourhood, pk=user)
    jobs = Business.objects.filter(neighbourhood=hood)
    return render(request, 'business.html', {'hood':hood, 'jobs':jobs})

@login_required
def post_news(request):
    userX = request.user
    user = Profile.objects.get(user=request.user)
    hood = Neighbourhood.objects.get(profile=user)
    
    if request.method == "POST":
        
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            data = form.save(commit=False)
            data.profile = user
            data.neighbourhood = hood
            data.save()
            return redirect('/')
        else:
            return False
    
    return render(request, 'post.html', {'form':PostForm})

@login_required
def neighbourhood(request, username):
    user = request.user
    neighbour = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST)
        prof = ProfileForm(request.POST, request.FILES)
        if form.is_valid() and prof.is_valid():
            hood = form.save()
            my_prof = prof.save(commit=False)
            my_prof.user = user
            my_prof.neighbourhood = hood
            my_prof.save()
            return redirect('/')
    else:
        form = NeighbourhoodForm()
        prof = ProfileForm()
    return render(request, 'hood.html', {'form': NeighbourhoodForm, 'prof':ProfileForm})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            
            # return HttpResponseRedirect(reverse('welcome'))
            return redirect('welcome')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': SignUpForm})

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

def welcome(request):
    return render(request, 'welcome.html')