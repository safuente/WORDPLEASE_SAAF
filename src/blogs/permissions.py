from rest_framework.permissions import BasePermission



class BlogsPermission(BasePermission):

    def has_permission(self, request, view):

        from blogs.api import PostDetailAPI
        if request.method == "POST" or request.user.is_superuser:
            return True

        if request.user.is_authenticated or request.method == "GET" and isinstance(view, PostDetailAPI):
            return True

        return request.method == "PUT" or (request.method == "PUT" or request.method == "DELETE")

    def has_object_permission(self, request, view, obj):

        return request.user == obj.user or request.user.is_superuser