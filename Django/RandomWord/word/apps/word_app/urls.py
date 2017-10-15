from django.conf.urls import url
from django.contrib import admin
from . import views #'.' means the same folder

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^generate/$', views.generate), 
    url(r'^clear/$', views.clear)
]
