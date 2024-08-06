from rest_framework.permissions import BasePermission


class IsLibrarian(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Librarian').exists()


class IsReader(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Readers').exists()


class IsModer(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Moder').exists()
