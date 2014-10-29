from django.db import models


class ForeignRepo(models.Model):
	"""
	Represents one instance of a foreign app repository (Google Play, Apple App Store, etc.)

	Fields:
		name   : The name of this repository
			(Google Play Store)

		url    : The main URL entry-point URL
			(https://play.google.com)

		app_url: The url pattern that each application will have, the position of each app id
			in the url will be replaced with the text "{APP_ID}".
			(https://play.google.com/store/apps/details?id={APP_ID})
	"""

	name = models.CharField(max_length=70)
	url = models.CharField(max_length=120)
	app_url = models.CharField(max_length=120)

	def __str__(self):
		return self.name


class Application(models.Model):
	name = models.CharField(max_length=120)

	def __str__(self):
		return self.name


class ForeignApplication(models.Model):
	repository = models.ForeignKey(ForeignRepo)
	application = models.ForeignKey(Application)
	url = models.CharField(max_length=120)

	def __str__(self):
		return '{} on {}'.format(self.application, self.repository)
