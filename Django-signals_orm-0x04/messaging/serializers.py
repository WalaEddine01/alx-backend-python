from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Conversation, Message

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone_number = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_number']

class MessageSerializer(serializers.ModelSerializer):
    message_body = serializers.CharField()
    sent_at = serializers.DateTimeField()
    sender = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['message_id', 'message_body', 'sent_at', 'sender']

class ConversationSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'users', 'messages']

    def get_messages(self, obj):
        messages = obj.messages.all().order_by('sent_at')
        return MessageSerializer(messages, many=True).data

    def validate_users(self, value):
        if not value or len(value) < 2:
            raise serializers.ValidationError("A conversation must include at least two users.")
        return value
