from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile/profile.html')

def business(request):
    return render(request, 'business.html')