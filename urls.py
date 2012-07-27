from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
     #url(r'^gbs/$', 'gbs.ceses.views.index'),
     url(r'^gbs/', include('gbs.cases.urls')),
    #url(r'^gbs/(?P<case_id>\d+)/$', 'gbs.cases.views.detail2'),
    url(r'^gbs/(?P<case_id>\d+)/$', 'django.views.generic.list_detail.object_list'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
