from rest_framework import permissions


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated) and (
            (request.user.is_admin)
            or (request.user.is_staff)
            or (request.user.is_superuser)
        )

    def has_object_permission(self, request, view, obj):
        return (request.user.is_authenticated) and (
            (request.user.is_admin)
            or (request.user.is_staff)
            or (request.user.is_superuser)
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or (
            request.user.is_authenticated and request.user.is_admin
        )


class isOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS) or (
            request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if not request.user.is_authenticated:
            return False

        return (
            obj.author == request.user
            or request.user.is_moderator
            or request.user.is_admin
        )
