from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

class Blog(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT)
    title = models.CharField(max_length=50)
    summary = models.CharField(max_length=150)
    body = models.CharField(max_length=400)
    image = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)  # saves the date when the object is created
    modified_at = models.DateTimeField(auto_now=True)  # saves the date when the object is updated

    category = models.ForeignKey(Category, on_delete=models.PROTECT)



