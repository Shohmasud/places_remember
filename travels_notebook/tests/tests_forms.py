from unittest import TestCase
from travels_notebook.forms import AddPostForm, SearchForms


class TestUrls(TestCase):

    def test_add_post_form(self):
        place = {'slug': 'armenia', 'description': 'Very nice'}
        form = AddPostForm(data=place)

        self.assertEquals(form.is_valid(), True)

    def test_search_address_form(self):
        place = {'name': 'London'}
        form = SearchForms(data=place)

        self.assertEquals(form.is_valid(), True)
