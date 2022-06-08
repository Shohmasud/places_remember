from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView


# Create your views here.
class LoginUsers(View):
    """The registration class that returns the registration template"""