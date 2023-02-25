from rest_framework.permissions import IsAuthenticatedOrReadOnly

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

class IsAuthenticatedAdmin(IsAuthenticatedOrReadOnly):
    def has_permission(self, request, view):
        """
        Method to check Admin permission.
        """
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
            and request.user.isAdmin
        )
