from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm


def home_page(request):
    posts = Post.objects.all()[:3]
    return render(request, 'blog/index.html', {'posts': posts})


def post_list(request):
    posts = Post.objects.all()
    date_filter = request.GET.get('date')
    if date_filter:
        posts = posts.filter(created_at__date=date_filter)
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_add(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})
