from django.shortcuts import render
from django.http import HttpResponse


def TestApp(request):
    return HttpResponse('Hello Word')


def TestView(request):
    return HttpResponse('Hello View')