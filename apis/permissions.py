from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsTaskExecutorOrCoExecutorOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.user.is_staff
                or request.user.is_superuser
                or request.user == obj.main_executor
                or request.user in obj.co_executors.all())

    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and (request.user.is_staff or request.user.is_superuser)