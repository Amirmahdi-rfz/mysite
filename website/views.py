from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def about_view(request):
    return HttpResponse("<h1>About Us</h1>")

def index_view(request):
    return HttpResponse("<h1>index view</h1>")