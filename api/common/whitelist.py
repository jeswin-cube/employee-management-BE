from rest_framework.permissions import BasePermission

from config.settings import (
    X_ORIGIN_SECRET,
)


class HeaderWhitelist(BasePermission):
    def __init__(self, secret=None):
        if secret:
            self.secret = secret
        else:
            self.secret = X_ORIGIN_SECRET

    def has_permission(self, request, view):
        return request.META.get("HTTP_X_ORIGIN_SECRET", None) == self.secret
