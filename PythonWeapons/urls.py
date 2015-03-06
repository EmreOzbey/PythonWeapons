from django.conf.urls import patterns, include, url
from django.contrib import admin
from account.views import mydatetime

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PythonWeapons.views.home', name='home'),
    # url(r'^PythonWeapons/', include('PythonWeapons.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'kerem/$', mydatetime),
)
