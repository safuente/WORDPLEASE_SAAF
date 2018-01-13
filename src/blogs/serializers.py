from rest_framework import serializers
from blogs.models import Blog, Post


class BlogsListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')



    class Meta:
        model = Blog
        fields = [ 'user','name','description','url']


class PostsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'image', 'summary', 'published_at']


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [ 'title','image','summary','published_at']


class PostDetailAllSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'

