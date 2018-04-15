from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
  url(r'^hello/','python.views.hello', name='hello'),
)
