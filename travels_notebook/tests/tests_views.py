from django.test import TestCase, Client
from django.urls import reverse
from travels_notebook.models import Places
from django.contrib.auth.models import User
from travels_notebook.utils import DataMixin


class TestView(TestCase,DataMixin):

    def setUp(self, **kwargs):
        self.client = Client()
        self.login_view = reverse('login')
        self.list_places = reverse('home')
        self.form_map = reverse('form-page', args=['london'])
        self.form_description = reverse('form-description', args=['london'])
        self.detail_post = reverse('show-post', args=['london'])
        self.user_admin = User.objects.create(username='admin1',
                                              email='postgres@localhost')
        self.places = Places.objects.create(name='London', slug='london',
                                            description='Very Nice',
                                            user=self.user_admin)

    def test_login_view_method_get(self):
        response = self.client.get(self.login_view)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'travels_notebook/'
                                          'html/login.html')

    def test_list_places_view_method_get(self):
        User.objects.create(username='admin2',
                            email='postgres@localhost')
        last_user = User.objects.all().last()
        response = self.client.get(self.list_places)
        Places.objects.create(name='Russia', slug='russia',
                              description='Very Nice',
                              user=last_user)
        Places.objects.create(name='USA', slug='usa',
                              description='Very Nice',
                              user=last_user)
        self.places = Places.objects.filter(
            user=last_user).count()
        self.assertEquals(self.places, 2)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'travels_notebook/'
                                          'html/home.html')

    def test_detail_post_view_method_get(self):
        response = self.client.get(self.detail_post)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'travels_notebook/html/'
                                          'description.html')

    def context_data(self, country):
        context = {'slug': self.get_address_map(country)}
        return context['slug']

    def test_form_map_view_method_get(self):
        response = self.client.get(self.form_map)
        map_html = {'map': self.get_address_map('London')}
        bool_maps = self.context_data('London') == map_html['map']
        self.assertEquals(bool_maps, False)
        response = self.client.get(self.form_map)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'travels_notebook/'
                                          'html/form_map.html')

    def test_form_map_view_method_post(self):
        address = {'name': 'London'}
        response = self.client.post(self.form_map,address)
        map_html = {'map': self.get_address_map(address['name'])}
        bool_maps = self.context_data(address['name']) == map_html['map']
        self.assertEquals(bool_maps, False)
        self.assertEquals(response.status_code, 302)

    def test_form_description_view_method_get(self):
        response = self.client.get(self.form_description)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'travels_notebook/'
                                          'html/form_description.html')

    def test_form_description_view_method_post(self):
        User.objects.create(username='admin6',
                            email='postgres@localhost')
        place = {'name': 'Armenia', 'slug': 'armenia',
                 'description': 'Very nice'}
        response = self.client.post(self.form_description, place)
        self.assertEquals(place['name'], 'Armenia')
        self.assertEquals(response.status_code, 302)
