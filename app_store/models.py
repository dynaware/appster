from django.db import models


class ForeignRepo(models.Model):
	name = models.CharField(max_length=70)
	url = models.TextField()


class ForeignApplication(models.Model):
	repository = models.ForeignKey(ForeignRepo)
	application = models.ForeignKey(Application)
	url = models.TextField()


class Application(models.Model):
	name = models.CharField(max_length=120)
