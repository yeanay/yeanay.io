from django.conf.urls import patterns, include, url

from ideology.views import congress

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^ideology/congress/(\d+)/(\w+)/', congress),

    # Examples:
    # url(r'^$', 'yeanay.views.home', name='home'),
    # url(r'^yeanay/', include('yeanay.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
