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
    """
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'password', 'phone_number']
        read_only_fields = ['user_id']
        extra_kwargs = {
            'email': {'required': True, 'allow_blank': False},
            'phone_number': {'required': True, 'allow_blank': False},
            'password': {'write_only': True, 'required': True, 'allow_blank': False}
        }

    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        if len(value) < 8:
            raise serializers.ValidationError("Phone number must be at least 8 digits long.")
        return value

    def create(self, validated_data):
        """
        Override create method to hash the password before saving.
        """
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user



class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Message model.
    """
    receiver = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    conversation = serializers.PrimaryKeyRelatedField(queryset=Conversation.objects.all())
    content = serializers.CharField()

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'receiver', 'conversation', 'content', 'sent_at']
        read_only_fields = ['message_id', 'sent_at', 'sender']

    def validate_content(self, value):
        if len(value.strip()) == 0:
            raise serializers.ValidationError("Message content cannot be empty.")
        return value
    
    def validate(self, data):
        user = self.context['request'].user
        if user == data.get('receiver'):
            raise serializers.ValidationError("Sender and receiver cannot be the same.")
        if not Conversation.objects.filter(conversation_id=data['conversation'].conversation_id, users=user).exists():
            raise serializers.ValidationError("You are not a participant in this conversation.")
        return data

    
    def perform_create(self, serializer):
        """
        Override perform_create to set the sender automatically.
        """
        serializer.save(sender=self.request.user)

class ConversationSerializer(serializers.ModelSerializer):
    """
    Serializer for Conversation model.
    Handles serialization and deserialization of conversation data.
    """
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'users', 'created_at', 'content']
        read_only_fields = ['conversation_id', 'created_at']
        extra_kwargs = {
            'name': {'required': True, 'allow_blank': False}
        }

    def validate_name(self, users):
        if not users:
            raise serializers.ValidationError("At least one user must be included in the conversation.")
        return users
