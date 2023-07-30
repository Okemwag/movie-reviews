from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    searchTerm = request.GET.get('searchMovie')
    return render(request, 'home.html', {'searchTerm': searchTerm})

def about(request):
    return HttpResponse('About Page')

def signup(request):
    email = request.GET.get('email')
    return render(request, 'signup.html', {'email':email})
