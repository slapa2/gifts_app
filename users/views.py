from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import CustomUser
from .forms import RegisterForm



class UserCreateView(CreateView):
    form_class = RegisterForm
    model = CustomUser
    template_name = 'registration/register.html'
    success_url = '/'