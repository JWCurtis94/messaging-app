from django.shortcuts import render, redirect
from .models import Message
from django.contrib.auth.forms import UserCreationForm
from .forms import MessageForm
from .models import Friendship
from .forms import FriendRequestForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request, 'messaging/homepage.html')

def message_list(request, user_id):
    messages = Message.objects.filter(receiver_id=user_id)
    return render(request, 'messaging/message_list.html', {'messages': messages})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('message_list')  # Redirect to the message list after sending
    else:
        form = MessageForm()
    return render(request, 'messaging/send_message.html', {'form': form})

def send_friend_request(request):
    if request.method == 'POST':
        form = FriendRequestForm(request.POST)
        if form.is_valid():
            friend_request = form.save(commit=False)
            friend_request.sender = request.user
            friend_request.save()
            return redirect('friend_requests')  # Redirect to friend requests page
    else:
        form = FriendRequestForm()
    return render(request, 'messaging/send_friend_request.html', {'form': form})

def friend_requests(request):
    received_requests = Friendship.objects.filter(receiver=request.user, status='requested')
    sent_requests = Friendship.objects.filter(sender=request.user, status='requested')
    return render(request, 'messaging/friend_requests.html', {
        'received_requests': received_requests,
        'sent_requests': sent_requests,
    })

def accept_friend_request(request, friend_request_id):
    friend_request = Friendship.objects.get(id=friend_request_id)
    if friend_request.receiver == request.user:
        friend_request.status = 'accepted'
        friend_request.save()
    return redirect('friend_requests')

def reject_friend_request(request, friend_request_id):
    friend_request = Friendship.objects.get(id=friend_request_id)
    if friend_request.receiver == request.user:
        friend_request.status = 'rejected'
        friend_request.save()
    return redirect('friend_requests')

@login_required
def profile(request):
    return render(request, 'messaging/profile.html', {'user': request.user})

@login_required
def message_list(request):
    sent_messages = Message.objects.filter(sender=request.user)
    received_messages = Message.objects.filter(receiver=request.user)
    return render(request, 'messaging/message_list.html', {
        'sent_messages': sent_messages,
        'received_messages': received_messages,
    })

@login_required
def accept_friend_request(request, friend_request_id):
    try:
        friend_request = Friendship.objects.get(id=friend_request_id, receiver=request.user)
        friend_request.status = Friendship.ACCEPTED
        friend_request.save()
    except Friendship.DoesNotExist:
        # Handle error (e.g., friend request not found)
        pass
    return redirect('friend_requests')

@login_required
def reject_friend_request(request, friend_request_id):
    try:
        friend_request = Friendship.objects.get(id=friend_request_id, receiver=request.user)
        friend_request.status = Friendship.REJECTED
        friend_request.save()
    except Friendship.DoesNotExist:
        # Handle error (e.g., friend request not found)
        pass
    return redirect('friend_requests')