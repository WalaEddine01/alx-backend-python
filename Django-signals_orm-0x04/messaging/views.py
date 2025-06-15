from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import render
from .models import Message
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message

@login_required
def unread_messages_view(request):
    user = request.user

    unread = Message.unread.unread_for_user(user)

    return render(request, 'messaging/unread.html', {'messages': unread})


@login_required
def delete_user(request):
    user = request.user
    logout(request)           # Log the user out first
    user.delete()             # Triggers the post_delete signal
    return redirect('home')   # Or any page you want

@login_required
def conversation_view(request):
    user = request.user

    # Fetch root messages only (not replies)
    root_messages = Message.objects.filter(
        receiver=user,
        parent_message__isnull=True
    ).prefetch_related(
        Prefetch('replies', queryset=Message.objects.select_related('sender', 'receiver'))
    ).select_related('sender', 'receiver')

    return render(request, 'messaging/conversation.html', {'messages': root_messages})
