from django import forms
from .models import Message
from .models import Friendship
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']

class FriendRequestForm(forms.ModelForm):
    class Meta:
        model = Friendship
        fields = ['receiver']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
