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
	url(r'review/(?P<app_id>\d+)/$', views.new_review, name='new_review'),
	url(r'new_app$', views.new_application, name='new_app'),
	url(r'review_apps$', views.review_applications, name='review_apps'),
	url(r'review_app/(?P<app_id>\d+)/(?P<choice>\d+)/$', views.review_application, name='review_app'),
	url(r'about$', views.about, name='about'),
	url(r'app_list_entry/(?P<app_id>\d+)/$', views.new_app_list_entry, name='new_app_list_entry'),
)
