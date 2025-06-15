from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Message, MessageHistory

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.id is None:
        return  # Skip if the message is being created, not edited

    try:
        old_message = Message.objects.get(id=instance.id)
        if old_message.content != instance.content:
            # Log the old content
            MessageHistory.objects.create(
                message=old_message,
                old_content=old_message.content
            )
            instance.edited = True
    except Message.DoesNotExist:
        pass  # In case it’s a new object that somehow has an ID
