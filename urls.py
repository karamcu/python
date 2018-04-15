from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
  url(r'^hello/','python.app.hello', name='hello'),
)
