from django.conf.urls import url
from django.contrib import admin
from . import views #'.' means the same folder

urlpatterns = [
    url(r'^index/', views.index), url(r'^create/', views.create), url(r'^(?P<number>[0-9]+)/$', views.show), url(r'^destroy/', views.destroy)
]



