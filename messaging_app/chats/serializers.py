"""
serializers module for the messaging app's chat functionality.
This module contains serializers for handling chat-related data,
including user, conversation, and message data.
"""

from rest_framework import serializers
from .models import User, Conversation, Message


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for User model.
    Handles serialization and deserialization of user data.
    Includes full name via SerializerMethodField.
    """
    full_name = serializers.SerializerMethodField()
    phone_number = serializers.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number', 'full_name']
        read_only_fields = ['user_id']
        extra_kwargs = {
            'email': {'required': True, 'allow_blank': False},
            'phone_number': {'required': True, 'allow_blank': False}
        }

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        if len(value) < 8:
            raise serializers.ValidationError("Phone number must be at least 8 digits long.")
        return value


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Message model.
    """
    sender = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    conversation = serializers.PrimaryKeyRelatedField(queryset=Conversation.objects.all())
    content = serializers.CharField()

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'receiver', 'conversation', 'content', 'sent_at']
        read_only_fields = ['message_id', 'sent_at']

    def validate_content(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Message content cannot be empty.")
        return value


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

    def validate_name(self, value):
        if len(value.strip()) < 3:
            raise serializers.ValidationError("Conversation name must be at least 3 characters long.")
        return value
