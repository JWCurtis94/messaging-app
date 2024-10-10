from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Message, Friendship
from django.contrib.auth.forms import UserCreationForm
from .forms import MessageForm, FriendRequestForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request, 'base.html')

def homepage(request):
    return render(request, 'messaging/homepage.html')

@login_required
def message_list(request):
    sent_messages = Message.objects.filter(sender=request.user)
    received_messages = Message.objects.filter(receiver=request.user)
    return render(request, 'messaging/message_list.html', {
        'sent_messages': sent_messages,
        'received_messages': received_messages,
    })

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()
            return redirect('message_list')
    else:
        form = MessageForm()
    return render(request, 'messaging/send_message.html', {'form': form})

@login_required
def send_friend_request(request):
    if request.method == 'POST':
        form = FriendRequestForm(request.POST)
        if form.is_valid():
            friend_request = form.save(commit=False)
            friend_request.sender = request.user
            friend_request.save()
            return redirect('friend_requests')
    else:
        form = FriendRequestForm()
    return render(request, 'messaging/send_friend_request.html', {'form': form})

@login_required
def friend_requests(request):
    received_requests = Friendship.objects.filter(receiver=request.user, status='requested')
    sent_requests = Friendship.objects.filter(sender=request.user, status='requested')
    return render(request, 'messaging/friend_requests.html', {
        'received_requests': received_requests,
        'sent_requests': sent_requests,
    })

@login_required
def accept_friend_request(request, friend_request_id):
    try:
        friend_request = Friendship.objects.get(id=friend_request_id, receiver=request.user)
        friend_request.status = Friendship.ACCEPTED
        friend_request.save()
    except Friendship.DoesNotExist:
        pass
    return redirect('friend_requests')

@login_required
def reject_friend_request(request, friend_request_id):
    try:
        friend_request = Friendship.objects.get(id=friend_request_id, receiver=request.user)
        friend_request.status = Friendship.REJECTED
        friend_request.save()
    except Friendship.DoesNotExist:
        pass
    return redirect('friend_requests')

@login_required
def profile(request):
    return render(request, 'messaging/profile.html', {'user': request.user})