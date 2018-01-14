# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, PasswordInput


class LoginForm(forms.Form):

    login_username = forms.CharField(label="Username")
    login_password = forms.CharField(widget=forms.PasswordInput(), label="Password")

class SignUpForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name','last_name','email']
        widgets = {
            'password': PasswordInput(),
        }

