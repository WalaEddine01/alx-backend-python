from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

# Custom user model
class CustomUser(AbstractUser):
    # Add extra fields later if needed (bio, profile pic, etc.)
    pass


# Conversation model (many-to-many between users)
class Conversation(models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.id}"


# Message model (belongs to conversation, has sender)
class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.sender.username} in {self.conversation.id}: {self.content[:30]}"
