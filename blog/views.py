from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


def home_page(request):
    posts = Post.objects.all()[:3]
    return render(request, 'blog/index.html', {'posts': posts})


def post_list(request):
    posts = Post.objects.all()
    date_filter = request.GET.get('date')
    if date_filter:
        posts = posts.filter(created_at__date=date_filter)
    return render(request, 'blog/post_list.html', {'posts': posts})
