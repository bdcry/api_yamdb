from rest_framework import permissions
from .models import CustomUser


class IsAuthorOrStaffOrReadOnly(permissions.BasePermission):
        def has_object_permission(self, request, view, obj):
            return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user
                or request.user.is_admin
                or request.user.is_moderator)


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
            and request.user.is_admin
            or request.user.is_superuser
        )


class IsAdminRole(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_superuser
        or request.user.is_admin
    )
