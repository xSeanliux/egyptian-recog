# -*- coding: utf-8 -*-
from django.http import HttpResponse

def hello(request, name):
    return HttpResponse('Hello, ' + str(name))

def add(request, a, b):
    s = int(a) + int(b)
    return HttpResponse(s)