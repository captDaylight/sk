from django.conf.urls.defaults import *
from auth.views import *

urlpatterns = patterns('',
	(r'^$', login_redirect),
	(r'^logout/$', logout_page),
	(r'^signup/$', sign_up),
)