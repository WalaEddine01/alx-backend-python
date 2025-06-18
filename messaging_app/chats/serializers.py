"""
serializers module for the messaging app's chat functionality.
This module contains serializers for handling chat-related data,
including user, conversation, and message data.
"""
from rest_framework import serializers
from messaging_app.chats.models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    Handles serialization and deserialization of user data.
    """
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number']
        read_only_fields = ['user_id']
        extra_kwargs = {
            'email': {'required': True, 'allow_blank': False},
            'phone_number': {'required': True, 'allow_blank': False}
        }


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Message model.
    """
    sender = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    conversation = serializers.PrimaryKeyRelatedField(queryset=Conversation.objects.all())

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'receiver', 'conversation', 'content', 'sent_at']
        read_only_fields = ['message_id', 'sent_at']
        extra_kwargs = {
            'content': {'required': True, 'allow_blank': False}
        }



class ConversationSerializer(serializers.ModelSerializer):
    """
    Serializer for Conversation model.
    Handles serialization and deserialization of conversation data.
    """
    users = UserSerializer(many=True, read_only=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'name', 'users', 'messages', 'created_at']
        read_only_fields = ['conversation_id', 'created_at']
        extra_kwargs = {
            'name': {'required': True, 'allow_blank': False}
        }
