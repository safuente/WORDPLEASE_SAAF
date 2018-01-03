from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        '''

        :return: name string representation
        '''

        return self.name

class Blog(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        '''

        :return: name string representation
        '''

        return self.name


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=50)
    summary = models.TextField()
    body = models.TextField()
    image = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)  # saves the date when the object is created
    modified_at = models.DateTimeField(auto_now=True)  # saves the date when the object is updatedwocd

    category = models.ManyToManyField(Category)

    def __str__(self):
        '''

        :return: name string representation
        '''

        return self.title


