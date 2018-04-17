#!/usr/bin/env python
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
  url(r'^hello/','views.hello', name='hello'),
)
