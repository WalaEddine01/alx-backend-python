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
from django.views.decorators.cache import cache_page


@cache_page(60)  # ✅ cache for 60 seconds
def conversation_messages(request):
    messages = Message.objects.all().order_by('-timestamp')
    return render(request, 'chats/conversation.html', {'messages': messages})

@login_required
def unread_messages_view(request):
    user = request.user

    unread_messages = Message.unread_messages.unread_for_user(user)
    unread = Message.unread.unread_for_user(user).only('id', 'content', 'timestamp')

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
