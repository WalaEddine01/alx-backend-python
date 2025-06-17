from django.db import models
from django.contrib.auth.models import User

class Conversation(models.Model):
    """
    """
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='converstaion')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    """
    """
    Conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp}"

