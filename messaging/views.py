from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .models import Message, Friendship
from .forms import MessageForm, FriendRequestForm, CustomUserCreationForm


def base(request):
    return render(request, 'base.html')


def homepage(request):
    return render(request, 'messaging/homepage.html')


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        # Redirect the user to their messages page after login
        return reverse_lazy('message_list', kwargs={'user_id': self.request.user.id})


@login_required
def message_list(request, user_id):
    user = get_object_or_404(User, id=user_id)  # Fetch the user by user_id
    sent_messages = Message.objects.filter(sender=user)  # Fetch sent messages
    received_messages = Message.objects.filter(receiver=user)  # Fetch received messages
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
            return redirect('message_list', user_id=user.id)  # Redirect to message list after signup
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
            return redirect('message_list', user_id=request.user.id)
    else:
        form = MessageForm()
    return render(request, 'messaging/send_message.html', {'form': form})


@login_required
def send_friend_request(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        try:
            receiver = User.objects.get(username=username)
            if receiver != request.user:
                Friendship.objects.create(sender=request.user, receiver=receiver, status='requested')
                return redirect('friend_requests')
            else:
                messages.error(request, "You cannot send a friend request to yourself.")
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")
    return redirect('friend_requests')



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
