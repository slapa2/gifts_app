from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from gift_lists.models import GiftList, Gift


class FriendGiftListListView(ListView):

    model = GiftList
    template_name = 'friend/friend_gift_list_list.html'

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
    template_name = 'friend/friend_gift_list_detail.html'

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
    template_name = 'friend/friend_gift.html'

    extra_context = {
        'friend_lists': 'active'
    }

    def get_queryset(self):
        return super().get_queryset().filter(gift_list__shared_to=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
