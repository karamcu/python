from django.http import HttpResponse
from django.conf.urls import patterns, include, url

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)


urlpatterns = patterns('',
  url(r'^hello/','myapp.app.hello', name='hello'),
)
