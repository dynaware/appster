from django.conf.urls import patterns, url

from app_store import views

urlpatterns = patterns(
	'',
	url(r'^$', views.index, name='index'),
	url(r'^app/(?P<app_id>\d+)/$', views.detail, name='detail'),
	url(r'^category/(?P<category_id>\d+)/$', views.category, name='category'),
	url(r'^categories$', views.categories, name='categories'),
	url(r'^search$', views.search, name='search'),
	url(r'^app_lists$', views.app_lists, name='app_lists'),
	url(r'app_list/(?P<list_id>\d+)/$', views.app_list, name='app_list'),
	url(r'app_list$', views.app_list, name='new_app_list'),
)
