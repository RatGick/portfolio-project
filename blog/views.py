from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.


def motherblog(request):
    posts = Blog.objects
    return render(request, 'blog/motherblog.html', {'posts': posts})


def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'post': detailblog})
