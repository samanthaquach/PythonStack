# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):

    return render(request, 'sessionWords_app/index.html')

def process(request):

    return redirect('/results')

def results(request):

    return render(request, 'sessionWords_app/result.html')
