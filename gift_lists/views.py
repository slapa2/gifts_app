from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import GiftList, Gift

class GiftListListView(ListView):
    model = GiftList
    template_name = 'gift_lists/gift_list_list.html'

    extra_context = {
        'my_lists': 'active'
    }
    
    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

class GiftListCreateView(CreateView):
    model = GiftList
    fields = ["name"]
    template_name = 'gift_lists/gift_list_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class GiftListDetailView(DetailView):
    model = GiftList
    template_name = 'gift_lists/gift_list_detail.html'

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
    template_name = 'gift_lists/gift.html'

    extra_context = {
        'my_lists': 'active'
    }

    def get_queryset(self):
        return super().get_queryset().filter(gift_list__owner=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.extra_context)
        return context

