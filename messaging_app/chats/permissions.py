from rest_framework import permissions
from django.contrib.auth.models import User
from .models import Conversation, Message

class IsConversationParticipant(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Conversation):
            return request.user in obj.users.all()
        elif isinstance(obj, Message):
            return request.user in obj.conversation.users.all()
        return False

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # For creating messages, check if user is in the conversation
        if view.basename == 'message':
            conversation_id = request.data.get('conversation')
            if not conversation_id:
                return False
            
            try:
                conversation = Conversation.objects.get(pk=conversation_id)
                return request.user in conversation.users.all()
            except Conversation.DoesNotExist:
                return False
        
        return True

class IsMessageSender(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user in obj.conversation.users.all()
        return obj.sender == request.user