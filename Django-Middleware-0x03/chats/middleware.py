import logging
from datetime import datetime
from django.utils.deprecation import MiddlewareMixin

class RequestLoggingMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        # Set up logging configuration
        self.logger = logging.getLogger('request_logger')
        self.logger.setLevel(logging.INFO)
        
        # Create file handler
        handler = logging.FileHandler('requests.log')
        handler.setLevel(logging.INFO)
        
        # Create formatter and add it to the handler
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        
        # Add handler to logger
        self.logger.addHandler(handler)

    def __call__(self, request):
        # Log request details
        user = request.user.username if request.user.is_authenticated else 'Anonymous'
        self.logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        
        # Process the request
        response = self.get_response(request)
        
        # Log response status
        self.logger.info(f"{datetime.now()} - User: {user} - Path: {request.path} - Status: {response.status_code}")
        
        return response