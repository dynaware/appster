from django import forms

from app_store import models


class AppListForm(forms.ModelForm):
	class Meta:
		model = models.ApplicationList
		fields = ['name', 'image']
		exclude = ['author']

