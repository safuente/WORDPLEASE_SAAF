from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Blog, Post


def home(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts': posts}
    return render(request, "posts_list.html", context)


def blog_list(request):
    blogs_list = Blog.objects.all()
    context ={'blogs': blogs_list}
    return render(request,"blog_home.html", context)



def post_list(request, username):
    possible_posts = Post.objects.filter(user__username=username).order_by('-created_at')
    if len(possible_posts) == 0:
        return render(request, "404.html", status=404)
    else:
        posts= possible_posts
        context = {'posts': posts}
        return render(request, "posts_list.html", context)


def post_detail(request, username,pk):
    possible_posts = Post.objects.filter(pk=pk)
    if len(possible_posts) == 0:
        return render(request, "404.html", status=404)
    else:
        post_categories = Post.objects.get(pk=pk).category.all()
        post= possible_posts[0]
        categories = post_categories
        context = {'categories': categories, 'post': post}
        return render(request, "post_detail.html", context)


