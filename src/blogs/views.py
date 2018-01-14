from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.utils import timezone
from blogs.forms import PostForm
from blogs.models import Blog, Post


def home(request):
    posts = Post.objects.all().order_by('-published_at').filter(published_at__lte=timezone.now())
    context = {'posts': posts[:5]}
    return render(request, "posts_list.html", context)


def blog_list(request):
    blogs_list = Blog.objects.all()
    context ={'blogs': blogs_list}
    return render(request,"blog_home.html", context)


def post_list(request, username):
    possible_posts = Post.objects.filter(user__username=username).order_by('-published_at')
    if len(possible_posts) == 0:
        return render(request, "404.html", status=404)
    else:
        posts= possible_posts
        context = {'posts': posts}
        return render(request, "posts_list.html", context)


def post_detail(request, username,pk):
    possible_posts = Post.objects.filter( pk=pk)
    if len(possible_posts) == 0:
        return render(request, "404.html", status=404)
    else:
        post_categories = Post.objects.get(pk=pk).category.all()
        post= possible_posts[0]
        categories = post_categories

        context = {'categories': categories, 'post': post}

        return render(request, "post_detail.html", context)


class CreatePostView(LoginRequiredMixin,View):
    def get(self, request):
        form = PostForm()
        return render(request, "post_form.html", {'form': form})


    def post(self, request):
        blog_post = Post()
        blog_post.user = request.user
        form = PostForm(request.POST, instance=blog_post)
        if form.is_valid():
            post = form.save()
            form = PostForm()
            url = reverse("post_detail_page", args=[request.user, post.pk])
            message = "Post created successfully! "
            message += '<a href="{0}">View</a>'.format(url)
            messages.success(request, message)
        return render(request, "post_form.html", {'form': form})
