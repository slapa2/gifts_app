from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import GiftList, Gift

class GiftListListView(ListView):
    model = GiftList
    template_name = 'gift_list/gift_list_list.html'

    extra_context = {
        'my_lists': 'active'
    }
    
    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

class GiftListDetailView(DetailView):
    model = GiftList
    template_name = 'gift_list/gift_list_detail.html'

    extra_context = {
        'my_lists': 'active'
    }

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

class GiftDetailView(DetailView):
    model = Gift
    template_name = 'gift_list/gift.html'

    extra_context = {
        'my_lists': 'active'
    }

    def get_queryset(self):
        return super().get_queryset().filter(gift_list__owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

class FriendGiftListListView(ListView):

    model = GiftList
    template_name = 'gift_list/friend/friend_gift_list_list.html'

    extra_context = {
        'friend_lists': 'active'
    }

    def get_queryset(self):
        return super().get_queryset().filter(shared_to=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

class FriendGiftListDetailView(DetailView):
    model = GiftList
    template_name = 'gift_list/friend/friend_gift_list_detail.html'

    extra_context = {
        'friend_lists': 'active'
    }

    def get_queryset(self):
        return super().get_queryset().filter(shared_to=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

class FriendGiftDetailView(DetailView):
    model = Gift
    template_name = 'gift_list/friend/friend_gift.html'

    extra_context = {
        'friend_lists': 'active'
    }

    def get_queryset(self):
        return super().get_queryset().filter(gift_list__shared_to=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
