from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
import django_filters.rest_framework
from messaging_app.chats.filters import MessageFilter
from django.shortcuts import get_object_or_404
from .models import Conversation, Message
from .serializers import MessageSerializer
from .permissions import IsParticipantOfConversation

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, IsParticipantOfConversation]
    filter_backends = [
        filters.OrderingFilter,
        django_filters.rest_framework.DjangoFilterBackend
    ]
    filterset_class = MessageFilter
    ordering_fields = ['sent_at', 'sender']
    search_fields = ['message_body']

    def get_queryset(self):
        conversation_id = self.request.query_params.get('conversation')
        if conversation_id:
            try:
                conversation = Conversation.objects.get(pk=conversation_id)
                if conversation.users.filter(pk=self.request.user.pk).exists():
                    return Message.objects.filter(conversation=conversation)
                return Message.objects.none()
            except Conversation.DoesNotExist:
                return Message.objects.none()
        return Message.objects.filter(sender=self.request.user)

    def create(self, request, *args, **kwargs):
        conversation_id = request.data.get('conversation')
        message_body = request.data.get('message_body')
        
        if not conversation_id or not message_body:
            return Response(
                {"error": "Conversation ID and message body are required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            conversation = Conversation.objects.get(pk=conversation_id)
            if not conversation.users.filter(pk=request.user.pk).exists():
                return Response(
                    {"error": "You are not a participant in this conversation."},
                    status=status.HTTP_403_FORBIDDEN
                )
            
            message = Message.objects.create(
                conversation=conversation,
                sender=request.user,
                message_body=message_body
            )
            
            serializer = self.get_serializer(message)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Conversation.DoesNotExist:
            return Response(
                {"error": "Conversation not found"},
                status=status.HTTP_404_NOT_FOUND
            )