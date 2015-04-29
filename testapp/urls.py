from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openfireapp.views.index', name='index'),
    url(r'^edit/(?P<username>.*)/$', 'openfireapp.views.edituser', name='edituser'),
    url(r'^create/$', 'openfireapp.views.createNewUser', name='createNewUser'),
    url(r'^delete/(?P<username>.*)/$', 'openfireapp.views.deleteUser', name='deleteUser'),
    url(r'^lock/(?P<username>.*)/$', 'openfireapp.views.lockUser', name='lockUser'),
    url(r'^unlock/(?P<username>.*)/$', 'openfireapp.views.unlockUser', name='unlockUser'),
    url(r'^viewfriends/(?P<username>.*)/$', 'openfireapp.views.viewfriends', name='viewfriends'),
    # url(r'^testapp/', include('testapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
