from datetime import datetime, time
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin

class RestrictAccessByTimeMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        # Set up allowed hours (6AM to 9PM)
        self.allowed_start = time(6, 0)  # 6:00 AM
        self.allowed_end = time(21, 0)   # 9:00 PM

    def __call__(self, request):
        # Get current time
        current_time = datetime.now().time()
        
        # Check if current time is outside allowed hours
        if not (self.allowed_start <= current_time <= self.allowed_end):
            return HttpResponseForbidden(
                "Chat access is only available between 6AM and 9PM"
            )
        
        # If time is within allowed range, continue with the request
        return self.get_response(request)