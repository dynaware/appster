from django.db import models


class Category(models.Model):
	"""
	Represents one instance of a category (game, book, utility, etc.)

	Fields:
		title:
			The name of this category
			(games, books, utilities)
	"""
	title = models.CharField(max_length=20)

	def __str__(self):
		return self.title


class ForeignRepo(models.Model):
	"""
	Represents one instance of a foreign app repository (Google Play, Apple App Store, etc.)

	Fields:
		name:
			The name of this repository
			(Google Play Store)

		url:
			The main URL entry-point URL
			(https://play.google.com)

		app_url:
			The url pattern that each application will have, the position of each app id
			in the url will be replaced with the text "{APP_ID}".
			(https://play.google.com/store/apps/details?id={APP_ID})

		platform:
			the platform that this repository serves
			(Android)
	"""

	name = models.CharField(max_length=70)
	url = models.CharField(max_length=120)
	app_url = models.CharField(max_length=120)
	platform = models.CharField(max_length=120)

	def __str__(self):
		return self.name


class Application(models.Model):
	"""
	Represents one instance of an application

	Fields:
		name:
			The name of this application (Google Drive)

		description:
			The application's description

		category:
			The application's category
	"""
	name = models.CharField(max_length=120)
	description = models.TextField()
	category = models.ForeignKey(Category)

	@property
	def rating(self):
		ratings = [i.rating for i in self.review_set.all()]
		if len(ratings) == 0:
			return 0.0
		return sum(ratings) / len(ratings)

	def __str__(self):
		return self.name


class ForeignApplication(models.Model):
	"""
	Represents one instance of a link between an application and its foreign repository.

	Example:
		Google Drive is an Application, Google Drive on the Apple App Store is a ForeignApplication,
		Google Drive on the Google Play store is a ForeignApplication.

	Fields:
		repository:
			The ForeignRepo instance that this is stored on

		application:
			The Application that this is related to

		app_id:
			The text that will be substituted for APP_ID on the foreign repository's app_url
	"""
	repository = models.ForeignKey(ForeignRepo)
	application = models.ForeignKey(Application)
	app_id = models.CharField(max_length=120)

	def __str__(self):
		return self.repository.app_url.format(APP_ID=self.app_id)


class Review(models.Model):
	"""
	Single instance of an application's review.

	Fields:
		rating:
			The numeric representation of the rating, where rating R is 1<=R<=5

		application:
			The application that this review belongs to

		author:
			The user that created this review

		review_text:
			The text of this review, does not have to be filled.
	"""
	rating = models.SmallIntegerField()
	application = models.ForeignKey(Application)
	review_text = models.TextField(null=True)

	def save_model(self, request, obj, form, change):
		if getattr(obj, 'author', None) is None:
			obj.author = request.user
		obj.save()
