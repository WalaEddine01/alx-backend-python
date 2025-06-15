from rest_framework import permissions
from django.contrib.auth.models import User
from .models import Conversation, Message

class IsParticipantOfConversation(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow authenticated users only
        if not request.user.is_authenticated:
            return False
            
        # For creating messages, check if user is in the conversation
        if request.method == 'POST' and view.basename == 'message':
            conversation_id = request.data.get('conversation')
            if not conversation_id:
                return False
            
            try:
                conversation = Conversation.objects.get(pk=conversation_id)
                return request.user in conversation.users.all()
            except Conversation.DoesNotExist:
                return False
        
        return True

    def has_object_permission(self, request, view, obj):
        # Allow GET requests for participants
        if request.method in permissions.SAFE_METHODS:
            if isinstance(obj, Conversation):
                return request.user in obj.users.all()
            elif isinstance(obj, Message):
                return request.user in obj.conversation.users.all()
            return False
        
        # For PUT/PATCH/DELETE operations
        if isinstance(obj, Message):
            return obj.sender == request.user
        return False