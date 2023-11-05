"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from django.contrib.auth import views as auth_views
from .views import Home

from gift_lists.views import GiftListListView, GiftListCreateView, GiftListDetailView, GiftDetailView
from friend.views import FriendGiftListListView, FriendGiftListDetailView, FriendGiftDetailView



urlpatterns = [
    path('', Home.as_view(), name='home'),

    # gift_lists
    path("gift-list/", GiftListListView.as_view(), name='gift-list'),
    path("gift-list/add/", GiftListCreateView.as_view(), name='gift-list-add'),
    path("gift-list/<int:pk>", GiftListDetailView.as_view(), name='gift-list-detail'),
    path("gift/<int:pk>", GiftDetailView.as_view(), name='gift-detail'),

    # friend
    path("friend/gift-list-list/", FriendGiftListListView.as_view(), name='friend-gift-list'),
    path("friend/gift-list/<int:pk>/", FriendGiftListDetailView.as_view(), name='friend-gift-list-detail'),
    path("friend/gift/<int:pk>", FriendGiftDetailView.as_view(), name='friend-gift-detail'),

    # users
    path("account/login/", auth_views.LoginView.as_view(), name='login'),
    path("account/logout/", auth_views.LogoutView.as_view(), name='logout'),

    # other
    path('admin/', admin.site.urls),
]
