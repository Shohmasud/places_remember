from django.shortcuts import render
from django.views.generic import View, ListView, DetailView, CreateView
from travels_notebook.models import Places,User


# Create your views here.
class LoginUsers(View):
    """The registration class that returns
    the registration template"""

    def get(self, request):
        return render(request, 'travels_notebook/html/login.html')


class PlacesList(ListView):
    """This class creates a paginator and
    filters the places visited by the user"""
    paginate_by = 3
    model = Places
    template_name = 'travels_notebook/html/home.html'

    def get_queryset(self):
        return Places.objects.filter(user=User.objects.all().last())
