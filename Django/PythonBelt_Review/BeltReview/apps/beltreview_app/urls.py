from django.conf.urls import url
from django.contrib import admin
from . import views #'.' means the same folder

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^logout/$', views.clear, name="clear"),
    url(r'^AddBook/$', views.AddBookPage, name="addbook"),
    url(r'^Submitting/$', views.submitreview, name="submitreview"),


]