from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^sandbox$', 'django_sandbox.views.sandbox', name='sandbox'),
    url(r'^.*$', 'django_sandbox.views.sandbox_redirect'),
)
