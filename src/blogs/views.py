from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Blog, Post


def hello_world(request):
    return HttpResponse("Hello World!")


def home(request):
    blogs_list = Blog.objects.all()
    context ={'blogs': blogs_list}
    return render(request,"home.html", context)



def post_list(request, username):
    possible_posts = Post.objects.filter(user__username=username)
    print(possible_posts)
    if len(possible_posts) == 0:
        return render(request, "404.html", status=404)
    else:
        posts= possible_posts
        context = {'posts': posts}
        return render(request, "posts_list.html", context)


