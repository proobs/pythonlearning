from django.http import HttpResponse
from django.shortcuts import render

# all view functions should take a parameter
def index(request): 
    return HttpResponse('Hi guys')