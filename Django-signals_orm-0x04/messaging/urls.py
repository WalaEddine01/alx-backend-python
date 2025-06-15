from django.urls import path
from .views import delete_user, unread_messages_view, conversation_messages

urlpatterns = [
    path('delete-account/', delete_user, name='delete_user'),
    path('inbox/unread/', unread_messages_view, name='unread_inbox'),
    path('messages/unread/', unread_messages_view, name='unread_messages'),
    path('conversation/', conversation_messages, name='conversation'),

]
