from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    posts = Post.publish.all()
    per_page = 1
    paginator = Paginator(posts, per_page)
    page = request.GET.get('page')
# Create your views here.
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, id):
    posts = Post.publish.get(id=id)
    return render(request, 'blog/post/detail.html', {'posts': posts})
