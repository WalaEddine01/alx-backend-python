from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Message, MessageHistory, Notification

@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    # Delete notifications related to user
    Notification.objects.filter(user=instance).delete()

    # Delete messages where the user is sender or receiver
    messages = Message.objects.filter(sender=instance) | Message.objects.filter(receiver=instance)
    
    # Delete related message histories first (if not CASCADE)
    for msg in messages:
        MessageHistory.objects.filter(message=msg).delete()
    
    messages.delete()  # Now delete the messages
