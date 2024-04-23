from rest_framework.permissions import BasePermission


class IsMemberOrOwner(BasePermission):
    def has_permission(self, request, view):

        user = request.user

        print("Pasando por el permiso" ,  user)
        return True