from django.shortcuts import render
from .models import Message

# Create your views here.
def message_list(request, user_id):
    messages = Message.objects.filter(receiver_id=user_id)
    return render(request, 'messaging/message_list.html', {'messages': messages})