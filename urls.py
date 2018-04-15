from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
  url(r'^hello/','myapp.app.hello', name='hello'),
)
