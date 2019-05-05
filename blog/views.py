from django.shortcuts import render
from .models import Blog

# Create your views here.


def motherblog(request):
    posts = Blog.objects
    return render(request, 'blog/motherblog.html', {'posts': posts})
