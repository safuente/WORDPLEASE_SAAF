from rest_framework import status
from rest_framework.generics import get_object_or_404, ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from blogs.models import Blog, Post
from blogs.permissions import BlogsPermission
from blogs.serializers import BlogsListSerializer, PostsListSerializer, PostDetailSerializer, PostDetailAllSerializer
from rest_framework.response import Response
from django.utils import timezone




class BlogsListAPI(ListAPIView):
    queryset = Blog.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ["user__username"]
    search_fields = ["user__username"]


    #ordering_fields = ('user__username',)

    def get_serializer_class(self):
        return BlogsListSerializer



class PostsListUserAPI(ListAPIView):
    filter_backends = [SearchFilter, OrderingFilter]
    ordering_fields = ["title","published_at"]
    search_fields = ["title","body"]




    def get(self, request,username):
        if str(request.user) == username or request.user.is_superuser:
            queryset= Post.objects.all().order_by('-published_at').filter(user__username=username)
        else:
            queryset = Post.objects.all().order_by('-published_at').filter(published_at__lte=timezone.now(),user__username=username)
        queryset = self.filter_queryset(queryset)
        serializer = PostsListSerializer(queryset, many=True)

        return Response(serializer.data)


class PostsListAPI(APIView):

    def post(self, request):
        if request.user.is_authenticated:
            request.data['user']=request.user.id
            serializer = PostDetailAllSerializer(data=request.data)
            if serializer.is_valid():
                post = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "You do not have permission to perform this action."},status=status.HTTP_403_FORBIDDEN)


class PostDetailAPI(APIView):

    permission_classes = [BlogsPermission]

    def get(self, request,username, pk):
        post = get_object_or_404(Post, pk=pk,user__username=username)
        if post.published_at <= timezone.now():
            serializer = PostDetailAllSerializer(post)
            return Response(serializer.data)
        elif str(request.user) == username or request.user.is_superuser and post.published_at>= timezone.now():
            serializer = PostDetailAllSerializer(post)
            return Response(serializer.data)
        else:
            return Response({"detail": "You do not have permission to perform this action."},status=status.HTTP_403_FORBIDDEN)

    def put(self, request,username, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        serializer = PostDetailAllSerializer(post, data=request.data)
        if serializer.is_valid():
            post = serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request,username, pk):
        post = get_object_or_404(Post, pk=pk)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






