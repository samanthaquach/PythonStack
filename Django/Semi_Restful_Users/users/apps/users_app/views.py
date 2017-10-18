from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from models import User


def index(request):
    users = User.objects.all()
    print User.objects.all().values()

    context = {
        'users': users,
    }
    return render(request, 'users_app/index.html', context)

def addUser(request):

    return render(request, 'users_app/add.html')

def process(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']

    User.objects.create(first_name=first_name, last_name=last_name, email=email)

    return redirect("/")

def show(request, User_id):

    context = {
        'User': User.objects.get(id=User_id)

    }

    return render(request,'users_app/show.html', context)


def edit(request, User_id):
    context = {
    'User': User.objects.get(id=User_id)
    }
    return render(request, 'users_app/edit.html', context)

def update(request, User_id):
    print User_id
    person = User.objects.get(id=User_id)
    person.first_name = request.POST.get('first_name', "")
    person.last_name = request.POST.get('last_name', "")
    person.email = request.POST.get('email', "")
    person.save()
    
    return redirect("/")

def destroy(request, User_id):
    User.objects.get(id=User_id).delete()
    return redirect("/")