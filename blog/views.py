from django.shortcuts import render
from blog.models import *

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(upload_now=1)
    context = {
        "posts": posts,
    }
    return render(request, "blog/blog-home.html", context)

def blog_single(request):
    return render(request, "blog/blog-single.html")

def test(request):
    persons = Person.objects.all()
    context = {
        "persons": persons,
        }
    return render(request, "blog/test.html", context)



    