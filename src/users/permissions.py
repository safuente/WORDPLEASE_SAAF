from rest_framework.permissions import BasePermission



class UsersPermission(BasePermission):

    def has_permission(self, request, view):

        from users.api import UserDetailAPI
        if request.method == "POST" or request.user.is_superuser:
            return True

        if request.user.is_authenticated and request.method == "GET" and isinstance(view, UserDetailAPI):
            return True

        return request.method == "PUT" or (request.method == "PUT" or request.method == "DELETE")

    def has_object_permission(self, request, view, obj):
        """
        El usuario autenticado (request.user) solo puede trabajar con el usuario solicitado (obj) si es el mismo o es un administrador
        """
        return request.user == obj or request.user.is_superuser