from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
    blog = Blog.objects
    return render(request, 'blog/homepage.html', {'blog': blog})

def detail(request, slug):
    detailBlog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog/article.html', {
        'article': detailBlog
    })