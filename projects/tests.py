from django.test import TestCase, Client
from django.urls import resolve, reverse

from .views import index
from .models import Project
from .test_utils import *


class InitTestCase(TestCase):
    def test_sanity_check(self):
        self.assertAlmostEqual(1, 1)


class ResolveUrlTestCase(TestCase):
    def test_main_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)


class MainViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')

    def test_get_index(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)

    def test_index_dont_show(self):
        create_test_data()
        response = self.client.get(self.index_url)
        self.assertNotContains(response, 'proj3')

    def test_index_projects_order(self):
        create_test_data()
        response = self.client.get(self.index_url)
        correct_order = r'proj5(.|\n)*proj2(.|\n)*proj1(.|\n)*proj4'
        self.assertRegex(response.content.decode("utf-8"), correct_order)

    def test_shows_tags(self):
        create_test_data()
        response = self.client.get(self.index_url)
        self.assertContains(response, 'tag1')
        self.assertNotContains(response, 'tag3')

    def test_shows_links(self):
        create_test_data2()
        response = self.client.get(self.index_url)
        self.assertContains(response, 'link1')
        self.assertContains(response, 'target1')
        self.assertNotContains(response, 'link2')


class TagFilteringViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')

    def test_tag_filtering(self):
        create_test_data()
        response = self.client.get(self.index_url, {'tag': 'tag1'})
        self.assertContains(response, 'proj1')
        self.assertNotContains(response, 'proj2')
        self.assertNotContains(response, 'proj3')
        self.assertNotContains(response, 'proj4')
        self.assertContains(response, 'proj5')

    def test_tag_not_strict_filtering(self):
        create_test_data()
        response = self.client.get(self.index_url, {'tag': 'tag1'})
        correct_order = r'proj5(.|\n)*proj1(.|\n)*proj2(.|\n)*proj4'
