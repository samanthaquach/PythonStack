
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

def index(request):

    return render(request, 'booksAuthors_app/index.html')