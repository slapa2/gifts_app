from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import GiftList, Gift

class GiftListListView(ListView):
    model = GiftList
    template_name = 'gift_list/gift_list_list.html'
    
    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

class GiftListDetailView(DetailView):
    model = GiftList
    template_name = 'gift_list/gift_list_detail.html'

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

class GiftDetailView(DetailView):
    model = Gift
    template_name = 'gift_list/gift.html'

    def get_queryset(self):
        return super().get_queryset().filter(gift_list__owner=self.request.user)

class FriendGiftListListView(ListView):

    model = GiftList
    template_name = 'gift_list/friend_gift_list_list.html'

    def get_queryset(self):
        return super().get_queryset().filter(shared_to=self.request.user)

class FriendGiftListDetailView(DetailView):
    model = GiftList
    template_name = 'gift_list/friend_gift_list_detail.html'

    def get_queryset(self):
        return super().get_queryset().filter(shared_to=self.request.user)

class FriendGiftDetailView(DetailView):
    model = Gift
    template_name = 'gift_list/gift.html'

    def get_queryset(self):
        return super().get_queryset().filter(gift_list__shared_to=self.request.user)
