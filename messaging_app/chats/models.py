from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4


class User(models.Model):
    '''
    '''
    user_id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"


class Conversation(models.Model):
    """
    """
    conversation_id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='converstaion')
    participants = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    """
    """
    message_id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
    Conversation = sender = models.ForeignKey(User, on_delete=models.CASCADE)
    models.ForeignKey(Conversation, on_delete=models.CASCADE)
    message_body = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp}"

