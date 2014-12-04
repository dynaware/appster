from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from app_store.models import *


def dropbox():
	return Application.objects.get(name='Dropbox')


class TestApplicationModel(TestCase):
	def setUp(self):
		self.productivity = Category.objects.create(title='Productivity')
		self.dropbox = Application.objects.create(
			name='Dropbox',
			description='',
			category=self.productivity,
		)
		Application.objects.create(
			name='Google Drive',
			description='',
			category=self.productivity,
		)
		self.play_store = ForeignRepo.objects.create(
			name='Google Play Store',
			url='http://play.google.com',
			app_url='http://play.google.com/?app={APP_ID}',
			platform='Android'
		)

		self.foreign_app = ForeignApplication.objects.create(
			repository=self.play_store,
			application=self.dropbox,
			app_id='com.dropbox',
		)

	def test_application_ratings(self):
		for i in (1, 2, 3, 3, 3, 3, 4, 5, 5, 5):
			Review.objects.create(
				rating=i,
				application=self.dropbox,
			)
		self.assertEqual(self.dropbox.rating, 3.4)

	def test_foreign_repo_url(self):
		play_store_dropbox = self.foreign_app
		self.assertEqual(str(play_store_dropbox), 'http://play.google.com/?app=com.dropbox')

	def test_click_count(self):
		url = '/app/{}/'.format(self.dropbox.id)
		c = Client()

		for _ in range(100):
			c.get(url)

		self.assertEqual(dropbox().click_count, 100)


class TestPageRendering(TestCase):
	def setUp(self):
		self.productivity = Category.objects.create(title='Productivity')
		self.dropbox = Application.objects.create(
			name='Dropbox',
			description='',
			category=self.productivity,
		)
		self.app_list = ApplicationList.objects.create(
			name='My favorite apps',
			image='http://fromthebungalow.files.wordpress.com/2011/05/thumbs-up.jpg',
		)

		self.client = Client()

	def load_one_page(self, url, status=200):
		response = self.client.get(url)
		self.assertEqual(response.status_code, status)

	def test_index_page(self):
		self.load_one_page('/')

	def test_detail_page(self):
		self.load_one_page(reverse('detail', args=(self.dropbox.id,)))

	def test_category_page(self):
		self.load_one_page(reverse('category', args=(self.productivity.id,)))

	def test_categories_page(self):
		self.load_one_page(reverse('categories'))

	def test_search_page(self):
		self.load_one_page(reverse('search'))

	def test_app_lists_page(self):
		self.load_one_page(reverse('app_lists'))

	def test_app_list_page(self):
		self.load_one_page(reverse('app_list', args=(self.app_list.id,)))

	def test_review_page(self):
		self.load_one_page(reverse('new_review', args=(self.dropbox.id,)), status=302)

	def test_new_app_page(self):
		self.load_one_page(reverse('new_app'), status=302)

	def test_review_apps_page(self):
		self.load_one_page(reverse('review_apps'), status=302)

	def test_about_page(self):
		self.load_one_page(reverse('about'))
