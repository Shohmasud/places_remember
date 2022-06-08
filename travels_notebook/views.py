from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import NoReverseMatch

from travels_notebook.utils import DataMixin
from travels_notebook.forms import AddPostForm, SearchForms
from django.views.generic import View, ListView, DetailView, CreateView
from travels_notebook.models import Places, User


# Create your views here.
class LoginUsers(View):
    """The registration class that returns
    the registration template"""

    def get(self, request):
        return render(request, 'travels_notebook/'
                               'html/login.html')


class PlacesList(ListView):
    """This class creates a paginator and
    filters the places visited by the user"""

    paginate_by = 3
    model = Places
    template_name = 'travels_notebook/html/home.html'

    def get_queryset(self):
        return Places.objects.filter(
            user=User.objects.all().last())


class ShowPostRemember(DetailView):
    """This class displays the key element in detail"""

    model = Places
    template_name = 'travels_notebook/html/description.html'


class GetMap(DataMixin, CreateView):
    """This class gets the address from the user and you
     have them on the map"""

    form_class = SearchForms
    template_name = 'travels_notebook/html/form_map.html'

    def get_context_data(self, *, object_list=None, **item):
        context = super().get_context_data(**item)
        context['slug'] = self.kwargs['slug']
        context['map'] = self.get_address_map(self.kwargs['slug'])
        return context

    def form_valid(self, form):
        address_map = self.get_address_map(form.cleaned_data['name'])
        if address_map is None:
            return HttpResponse('ENTER THE ADDRESS OF THE FIELD CORRECTLY!')
        try:
            return redirect('form-page', slug=form.cleaned_data['name'])
        except NoReverseMatch:
            return HttpResponse('THE ADDRESS FIELD ALLOWS LATIN LETTERS, NUMBER, UNDERSCORES, SPACES')
