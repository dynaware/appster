from django import forms

from app_store import models


class ReviewForm(forms.ModelForm):
	class Meta:
		model = models.Review
		fields = ['rating', 'application', 'review_text']
