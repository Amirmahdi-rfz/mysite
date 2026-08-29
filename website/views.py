from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_view(request):
    return render(request, "home.html")

def about_view(request):
    return render(request, "about.html")

def index_view(request):
    return render(request, "index.html")