from django.conf.urls import patterns, url

from app_store import views

urlpatterns = patterns(
	'',
	url(r'^$', views.index, name='index'),
	url(r'^app/(?P<app_id>\d+)/$', views.detail, name='detail'),
	url(r'^category/(?P<category_id>\d+)/$', views.category, name='category'),
	url(r'^categories$', views.categories, name='categories'),
	url(r'^search$', views.search, name='search'),
)
