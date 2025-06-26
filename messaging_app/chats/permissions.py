from rest_framework import permissions

class IsSender(permissions.BasePermission):
    """
    Custom permission to allow only the sender of the message to modify it.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user

        # SAFE METHODS (GET, HEAD, OPTIONS): allow sender or receiver
        if request.method in permissions.SAFE_METHODS:
            return obj.sender == user or obj.receiver == user

        # WRITE METHODS (PUT, PATCH, DELETE): allow only sender
        return obj.sender == user
    
class IsSelf(permissions.BasePermission):
    """
    Allows users to only access their own user object.
    """

    def has_object_permission(self, request, view, obj):
        # Allow access if the user superuser
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            # Allow safe methods (GET, HEAD, OPTIONS) for the user object
            return obj == request.user
        return obj == request.user
    
class InConversation(permissions.BasePermission):
    """
    Custom permission to check if the user is part of the conversation.
    """

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user in obj.users.all()
