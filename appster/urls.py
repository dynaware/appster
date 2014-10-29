from django.conf.urls import patterns, include, url
from django.contrib import admin

import app_store.urls

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'appster.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^$', include(app_store.urls)),
)
