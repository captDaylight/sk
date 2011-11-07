from django.conf.urls.defaults import *
from django.conf import settings
from sk.views import * 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^login/', 'django.contrib.auth.views.login'),
	(r'^auth/', include('auth.urls')),

	(r'^$', landing),
	(r'^upload/$', upload),
	(r'^passport/(?P<user_id>\d+)/$', passport),	
	(r'^item/(?P<item_id>\d+)/$', item),
	(r'^follow/(?P<user_id>\d+)/$', follow),
	(r'^unfollow/(?P<user_id>\d+)/$', unfollow),
	(r'^vote/(?P<item_id>\d+)/(?P<user_id>\d+)/$', vote),
	(r'^fetch/(?P<item_type>[a-z]*)/$', fetch),

	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT }),
	(r'^comments/', include('django.contrib.comments.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
