from django.conf.urls import patterns, include, url
from django.contrib import admin
from twits.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitterclone.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	url(r'^(?P<user>.*)/$', profile, name = "profile"),
)

