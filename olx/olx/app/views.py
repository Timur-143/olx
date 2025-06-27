from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .forms import UserForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import User

class MainView(ListView):
    template_name = "main.html"
    context_object_name = 'test'
    model = User
class CreateUser(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("main")
    template_name = 'registration/reg.html'