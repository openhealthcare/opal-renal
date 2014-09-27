from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from opal.urls import urlpatterns as opatterns

from renal import views

urlpatterns = patterns(
    '',
    url(r'^test/500$', views.Error500View.as_view(), name='test-500'),
)

urlpatterns += opatterns

from django.conf import settings
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
