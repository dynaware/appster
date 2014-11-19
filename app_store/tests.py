from django.test import TestCase, Client
from app_store.models import *


def dropbox():
	return Application.objects.get(name='Dropbox')


class TestApplicationModel(TestCase):
	def setUp(self):
		Category.objects.create(title='Productivity')
		Application.objects.create(
			name='Dropbox',
			description='',
			category=Category.objects.get(title='Productivity')
		)
		Application.objects.create(
			name='Google Drive',
			description='',
			category=Category.objects.get(title='Productivity')
		)
		ForeignRepo.objects.create(
			name='Google Play Store',
			url='http://play.google.com',
			app_url='http://play.google.com/?app={APP_ID}',
			platform='Android'
		)

		play_store = ForeignRepo.objects.get(name='Google Play Store')

		ForeignApplication.objects.create(
			repository=play_store,
			application=dropbox(),
			app_id='com.dropbox',
		)

	def test_application_ratings(self):
		for i in (1, 2, 3, 3, 3, 3, 4, 5, 5, 5):
			Review.objects.create(
				rating=i,
				application=dropbox()
			)
		self.assertEqual(dropbox().rating, 3.4)

	def test_foreign_repo_url(self):
		play_store_dropbox = ForeignApplication.objects.get(app_id='com.dropbox')
		self.assertEqual(str(play_store_dropbox), 'http://play.google.com/?app=com.dropbox')

	def test_click_count(self):
		url = '/app/{}/'.format(dropbox().id)
		c = Client()

		for _ in range(100):
			c.get(url)

		self.assertEqual(dropbox().click_count, 100)
