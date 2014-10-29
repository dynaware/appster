from django.db import models


class ForeignRepo(models.Model):
	name = models.CharField(max_length=70)
	url = models.CharField(max_length=120)

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
