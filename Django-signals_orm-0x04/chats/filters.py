import django_filters
from django_filters import rest_framework as filters
from .models import Message

class MessageFilter(filters.FilterSet):
    sender = filters.NumberFilter(field_name='sender__id')
    conversation = filters.NumberFilter(field_name='conversation__id')
    sent_after = filters.DateTimeFilter(field_name='sent_at', lookup_expr='gte')
    sent_before = filters.DateTimeFilter(field_name='sent_at', lookup_expr='lte')
    
    class Meta:
        model = Message
        fields = ['sender', 'conversation', 'sent_after', 'sent_before']