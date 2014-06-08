from django.conf.urls.defaults import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'emirates.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^calculator/$', 'calculator.views.calculator', name='index'),
    url(r'^$', 'calculator.views.calculator', name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
