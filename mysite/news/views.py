from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(request)
    return HttpResponse('Hello world')


def test(request):
    return HttpResponse('<h1>Loloshka<h1>')
# Create your views here.

