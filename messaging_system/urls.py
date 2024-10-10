from django.urls import path, include
from messaging import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    
    # Message-related
    path('messages/<int:user_id>/', views.message_list, name='message_list'),
    path('send/', views.send_message, name='send_message'),

    # Friend-related
    path('send_friend_request/', views.send_friend_request, name='send_friend_request'),
    path('friend_requests/', views.friend_requests, name='friend_requests'),
    path('accept_friend_request/<int:friend_request_id>/', views.accept_friend_request, name='accept_friend_request'),
    path('reject_friend_request/<int:friend_request_id>/', views.reject_friend_request, name='reject_friend_request'),
    
    # Profile and homepage
    path('profile/', views.profile, name='profile'),
    path('', views.homepage, name='homepage'),

    # Include all default Django auth views like password reset, etc.
    path('accounts/', include('django.contrib.auth.urls')),
]