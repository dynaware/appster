from django.conf.urls import patterns, url

from user_auth import views

urlpatterns = patterns(
	'',
	url(r'^login$', views.login, name='login'),
)
