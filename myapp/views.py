from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hello(request):
	text ="""<h1> welcome to my app</h1>"""
	return HttpResponse(text)
def morning(request):
	text1 ="""<h2> welcome , this is morning.html test</h2>"""
	return HttpResponse(text1)
def viewArticle(request, articleId):
	text2 = "displaying article number: %s" %articleId
	return HttpResponse(text2)
def evening(request, month, year):
	text3 = "displaying month and year: %s %s"%(month, year)
	return HttpResponse(text3)
