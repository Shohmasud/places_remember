from django.test import TestCase
from travels_notebook.models import Places, User


class TestModels(TestCase):
    def setUp(self):
        self.user_admin = User.objects.create(username='admin1',
                                              email='postgres@localhost')
        self.address = Places.objects.create(name='Germany', slug='german',
                                             description='Very nice',
                                             user=self.user_admin)

    def test_place_models(self):
        get_place = Places.objects.get(id=self.address.pk)
        self.assertEquals(get_place.name,'Germany')
        self.assertEquals(get_place, self.address)
