"""
URL configuration for messaging_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from messaging import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('messages/<int:user_id>/', views.message_list, name='message_list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', auth_views.LoginView.as_view(), name='signup'),
    path('send/', views.send_message, name='send_message'),
    path('messages/', views.message_list, name='message_list'),
    path('send_friend_request/', views.send_friend_request, name='send_friend_request'),
    path('friend_requests/', views.friend_requests, name='friend_requests'),
    path('accept_friend_request/<int:friend_request_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('reject_friend_request/<int:friend_request_id>/', views.reject_friend_request, name='reject_friend_request'),
    path('profile/', views.profile, name='profile'),
    path('', views.homepage, name='homepage'),
]
