from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def home_page(request):
    posts = Post.objects.all()[:3]
    return render(request, 'pages/index.html', {'posts': posts})


def post_list(request):
    posts = Post.objects.all()
    date_filter = request.GET.get('date')
    if date_filter:
        posts = posts.filter(created_at__date=date_filter)
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('home')
