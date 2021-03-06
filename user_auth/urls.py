from django.conf.urls import patterns, url

from user_auth import views

urlpatterns = patterns(
	'',
	url(r'^login$', views.login_user, name='login'),
	url(r'^logout$', views.logout_user, name='logout'),
	url(r'^signup$', views.register_user, name='signup'),
	url(r'^user$', views.user, name='user'),
	url(r'^app_list$', views.app_list, name='new_app_list'),
)
