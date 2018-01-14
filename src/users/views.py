from django.contrib import messages
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from blogs.models import Blog
from users.forms import LoginForm, SignUpForm


class LoginView(View):

    def get(self, request):
        context = {'form': LoginForm()}
        return render(request, "login_form.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("login_username")
            password = form.cleaned_data.get("login_password")
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user and authenticated_user.is_active:
                django_login(request, authenticated_user)
                redirect_to = request.GET.get("next", "home_page")
                return redirect(redirect_to)
            else:
                form.add_error(None, "Usuario incorrecto o inactivo")
                messages.error(request, "Usuario incorrecto o inactivo")
        context = {'form': form}
        return render(request, "login_form.html", context)


class SignUpView(View):

    def get(self, request):
        context = {'form': SignUpForm()}
        return render(request, "signup_form.html", context)

    def post(self, request):
        user_post = User()
        form = SignUpForm(request.POST, instance= user_post)
        if form.is_valid():
            user_post.set_password(form.cleaned_data.get("password"))
            user_post = form.save()
            default_blog_name= "Weblog " + str(user_post.username)
            url = "/blogs/" + str(user_post.username)
            blog_default = Blog(description="",name="Weblog " + user_post.username,user=user_post, url=url)
            blog_default.save()
            form = SignUpForm()
            message = "User "+user_post.username+" registered successfully! "
            message+= "Your default blog name is "+ default_blog_name
            messages.success(request, message)
        context = {'form': form}
        return render(request, "signup_form.html", context)


def logout(request):
    django_logout(request)
    return redirect("login_page")
