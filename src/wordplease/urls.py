"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from blogs.views import home, post_list, post_detail, blog_list, CreatePostView
from users.views import LoginView, logout, SignInView

urlpatterns = [

    path('admin/', admin.site.urls),
    path('blogs/<username>', post_list, name="posts_list_page"),
    path('blogs/<username>/<int:pk>', post_detail, name="post_detail_page"),
    path('blogs/', blog_list, name="blog_home"),

    path('login/', LoginView.as_view(), name="login_page"),
    path('logout/', logout, name="logout_page"),
    path('signin/', SignInView.as_view(), name="signin_page"),
    path('new-post/',CreatePostView.as_view(), name="new_post"),
    path('', home, name="home_page")
]
