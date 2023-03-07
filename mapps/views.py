from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def ram(request):
    return HttpResponse('<h1>my name is ram sir</h1>')
def srujana(request):
    return HttpResponse('<marquee><h1>srujana thinnava ra</h1></marquee>')

