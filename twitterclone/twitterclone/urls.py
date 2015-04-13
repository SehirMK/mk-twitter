from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib import admin
from twits.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'twits.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^follow/(?P<f_id>.*)/(?P<f_id2>.*)/$', 'twits.views.follow', name = "follow"),
    url(r'^unfollow/(?P<f_id>.*)/(?P<f_id2>.*)/$', 'twits.views.unfollow', name = "unfollow"),
    url(r'^search/(?P<q>.*)/$', 'twits.views.search', name = "search"),
    url(r'^posttwit/', 'twits.views.posttwit'),
    url(r'^rt/(?P<t_id>.*)/$', 'twits.views.retweet', name = "retweet"),
    url(r'^fav/(?P<twit_id>.*)/$', 'twits.views.fav', name = "fav"),
	url(r'^admin/', include(admin.site.urls)),
	(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^(?P<user>.*)/fav/$', 'twits.views.favedtwits', name = "favedtwits"),
	url(r'^(?P<user>.*)/$', 'twits.views.profile', name = "profile"),



)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
	urlpatterns += patterns('django.contrib.staticfiles.views',
	url(r'^static/(?P<path>.*)$', 'serve'),
)

