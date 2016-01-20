from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drought.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('overview.urls')),
    url(r'^historical/', include('visualizer.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
