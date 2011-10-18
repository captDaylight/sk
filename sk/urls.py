from django.conf.urls.defaults import *
from django.conf import settings
from sk.views import * 

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),

	(r'^login/', 'django.contrib.auth.views.login'),
	(r'^auth/', include('auth.urls')),

	(r'^$', landing),
	(r'^upload/$', upload),
	(r'^passport/$', passport),	
	(r'^item/(?P<item_id>\d+)/$', item),
	(r'^follow/(?P<user_id>\d+)/$', follow),
	(r'^unfollow/(?P<user_id>\d+)/$', unfollow),

	url(r'^admin/', include(admin.site.urls)),
)
