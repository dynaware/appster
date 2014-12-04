from django.conf.urls import patterns, include, url
from django.contrib import admin

import app_store.urls
from appster import settings
import user_auth.urls

urlpatterns = patterns(
	'',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^auth/', include(user_auth.urls)),
	url(r'^', include(app_store.urls)),
	url(r'^$', include(app_store.urls)),
)

if not settings.DEBUG:
	urlpatterns += patterns(
		'',
		(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	)
