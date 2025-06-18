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
    filter_backends = ["first_name", "last_name", "email"]

    def get_queryset(self):
        return self.queryset.order_by('first_name')
    
class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Conversation model.
    Provides CRUD operations for conversation data.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    search_fields = ['name']

    def get_queryset(self):
        return self.queryset.order_by('name')
    
class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Message model.
    Provides CRUD operations for message data.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    search_fields = ['content']

    def get_queryset(self):
        return self.queryset.order_by('sent_at')
