from django import forms
from .models import Message
from .models import Friendship

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']

class FriendRequestForm(forms.ModelForm):
    class Meta:
        model = Friendship
        fields = ['receiver']
