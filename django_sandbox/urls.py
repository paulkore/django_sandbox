from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^sandbox$', 'django_sandbox.views.sandbox', name='sandbox'),
    url(r'^.*$', 'django_sandbox.views.sandbox_redirect'),
)
