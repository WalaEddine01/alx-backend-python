from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import logout

@login_required
def delete_user(request):
    user = request.user
    logout(request)           # Log the user out first
    user.delete()             # Triggers the post_delete signal
    return redirect('home')   # Or any page you want
