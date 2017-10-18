from django.conf.urls import url
from django.contrib import admin
from . import views #'.' means the same folder

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^results$', views.results),
   
]