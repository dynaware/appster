from django import forms

from app_store import models


class ReviewForm(forms.ModelForm):
	class Meta:
		model = models.Review
		fields = ['rating', 'review_text']
		exclude = ['application']


class NewApp(forms.ModelForm):
	class Meta:
		model = models.Application
		fields = ['name', 'description', 'category', 'screenshot', 'logo']
		exclude = ['approved']


class ApplicationListEntryForm(forms.ModelForm):
	class Meta:
		model = models.ApplicationListEntry
		fields = ['list']
		exclude = ['application']
