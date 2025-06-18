from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Conversation, Message
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User model.
    Provides CRUD operations for user data.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access

    def get_queryset(self):
        return self.queryset.order_by('first_name')
    
class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Conversation model.
    Provides CRUD operations for conversation data.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def get_queryset(self):
        return self.queryset.order_by('name')
    
class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Message model.
    Provides CRUD operations for message data.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        return self.queryset.order_by('sent_at')
