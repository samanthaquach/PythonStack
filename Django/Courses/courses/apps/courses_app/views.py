from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import Course

# Create your views here.

def index(request):


    all_courses = Course.objects.all()
    print all_courses

    context = {
        "courses":all_courses
    }


    return render(request, 'courses_app/index.html', context)


def create_new_course(request):
# -- Make a new course -----
    if request.method == "POST":
        print request.POST
        Course.objects.create(course_name=request.POST['course_name'], course_description=request.POST['course_description'])

    return redirect('/')


def show_delete_confirmation(request, course_id):
# -- Confirmation before delete ---
    course = Course.objects.get(pk=course_id)

    context = {
        "course":course
    }

    return render(request, "courses_app/confirmation_page.html", context)

def delete_course(request, course_id):
# -- Delete course -----
    Course.objects.get(pk=course_id).delete()

    return redirect('/')