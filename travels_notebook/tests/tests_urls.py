from django.test import SimpleTestCase
from django.urls import resolve, reverse
from travels_notebook.views import LoginUsers, PlacesList, \
    ShowPostRemember, GetMap, SaveForm


class TestUrls(SimpleTestCase):
    def test_login_view_url_resolve(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginUsers)

    def test_list_places_url_resolve(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, PlacesList)

    def test_form_map_url_resolve(self):
        url = reverse('form-page',args=['london'])
        self.assertEquals(resolve(url).func.view_class, GetMap)

    def test_create_form_description_url_resolve(self):
        url = reverse('form-description',args=['london'])
        self.assertEquals(resolve(url).func.view_class, SaveForm)

    def test_create_detail_post_view_url_resolve(self):
        url = reverse('show-post', args=['london'])
        self.assertEquals(resolve(url).func.view_class, ShowPostRemember)
