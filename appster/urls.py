from django.conf.urls import patterns, include, url
from django.contrib import admin

import app_store.urls

urlpatterns = patterns(
	'',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^app_store/', include(app_store.urls)),
	url(r'^$', include(app_store.urls)),
)
