from django.db import models


class ForeignRepo(models.Model):
	name = models.CharField(max_length=70)
	url = models.CharField(max_length=120)


class Application(models.Model):
	name = models.CharField(max_length=120)


class ForeignApplication(models.Model):
	repository = models.ForeignKey(ForeignRepo)
	application = models.ForeignKey(Application)
	url = models.TextField()


