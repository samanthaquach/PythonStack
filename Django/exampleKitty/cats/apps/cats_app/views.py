
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    response="made it to index"
    return HttpResponse(response)

def create(request):
   return redirect ('/cats/index')

def show(request, number):
    place_holder='your cat is '+str(number)
    return HttpResponse(place_holder)

def destroy(request):
    return redirect ('/cats/index')


