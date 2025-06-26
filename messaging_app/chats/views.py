from django.shortcuts import render
from rest_framework import viewsets, filters, status
from rest_framework.response import Response
from .models import User, Conversation, Message
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSender, IsSelf, InConversation
from django.db import models
from rest_framework import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet for User model.
    Provides CRUD operations for user data.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name', 'email']
    permission_classes = [IsSelf, IsAuthenticated]
    

    def get_queryset(self):
        return self.queryset.order_by('first_name')

    
class ConversationViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Conversation model.
    Provides CRUD operations for conversation data.
    """
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [InConversation, IsAuthenticated]
    

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def get_queryset(self):
        user = self.request.user
        return Conversation.objects.filter(users=user)

    def perform_create(self, serializer):
        conversation = serializer.save()
        conversation.users.add(self.request.user)


    
class MessageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Message model.
    Provides CRUD operations for message data.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['content', 'sender__first_name', 'receiver__first_name']
    permission_classes = [IsSender, IsAuthenticated]
    

    def get_queryset(self):
        """
        Override get_queryset to filter messages by the authenticated user.
        """
        user = self.request.user
        return Message.objects.filter(sender=user) | Message.objects.filter(receiver=user)

    def perform_create(self, serializer):
        """
        Override perform_create to set the sender automatically.
        """
        if 'sender' in serializer.validated_data:
            raise serializers.ValidationError("Sender should not be provided in the request data.")

        if serializer.validated_data.get('receiver') not in serializer.validated_data.get('conversation').users.all():
            raise serializers.ValidationError("Receiver must be part of the conversation.")
        
        if serializer.validated_data.get('sender') == serializer.validated_data.get('receiver'):
            raise serializers.ValidationError("Sender and receiver cannot be the same.")

        serializer.save(sender=self.request.user)            
