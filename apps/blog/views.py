from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    """Blog list page with categories"""
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog/list.html', {'posts': posts})


def post_detail(request, slug):
    """Blog detail page with newsletter CTA"""
    post = get_object_or_404(Post, slug=slug, is_published=True)
    return render(request, 'blog/detail.html', {'post': post})
