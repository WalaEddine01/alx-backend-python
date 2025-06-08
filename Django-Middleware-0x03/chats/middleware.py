import json
import logging
from datetime import datetime
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden

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

class OffensiveLanguageMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response
        # List of forbidden words
        self.offensive_words = [
            'badword1', 'badword2',  # Add your forbidden words here
        ]
        
        # Set up logging
        self.logger = logging.getLogger('offensive_content_logger')
        self.logger.setLevel(logging.INFO)
        
        # Create file handler
        handler = logging.FileHandler('offensive_content.log')
        handler.setLevel(logging.INFO)
        
        # Create formatter and add it to the handler
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        
        # Add handler to logger
        self.logger.addHandler(handler)

    def __call__(self, request):
        # Only check content for POST/PUT/PATCH requests
        if request.method in ['POST', 'PUT', 'PATCH']:
            try:
                # Get request content
                content = json.loads(request.body)
                
                # Check message content
                if 'message_body' in content:
                    message = content['message_body'].lower()
                    
                    # Check for offensive words
                    for word in self.offensive_words:
                        if word.lower() in message:
                            # Log the attempt
                            self.logger.info(
                                f"{datetime.now()} - User: {request.user.username} - "
                                f"Attempted to send offensive message: {message}"
                            )
                            return HttpResponseForbidden(
                                "Message contains forbidden content"
                            )
                
                # Check conversation description
                if 'description' in content:
                    description = content['description'].lower()
                    for word in self.offensive_words:
                        if word.lower() in description:
                            self.logger.info(
                                f"{datetime.now()} - User: {request.user.username} - "
                                f"Attempted to create conversation with offensive description: {description}"
                            )
                            return HttpResponseForbidden(
                                "Conversation description contains forbidden content"
                            )
                
            except json.JSONDecodeError:
                # Log invalid JSON
                self.logger.info(
                    f"{datetime.now()} - User: {request.user.username} - "
                    f"Invalid JSON content: {request.body}"
                )
                return HttpResponseForbidden("Invalid request format")
        
        # Log the request
        self.logger.info(
            f"{datetime.now()} - User: {request.user.username} - "
            f"Method: {request.method} - Path: {request.path}"
        )
        
        # Continue with the request
        return self.get_response(request)
    
