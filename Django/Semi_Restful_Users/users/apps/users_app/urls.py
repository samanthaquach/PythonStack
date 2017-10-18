from django.conf.urls import url
from django.contrib import admin
from . import views #'.' means the same folder

urlpatterns = [
    url(r'^$', views.index), 
    url(r'^addUser/$', views.addUser),
    url(r'^users/process/', views.process),
    url(r'^users/(?P<User_id>\d+)$', views.show), 
    url(r'^edit/(?P<User_id>\d+)$', views.edit),
    url(r'^users/(?P<User_id>\d+)/update$', views.update),
    url(r'^users/(?P<User_id>\d+)/destroy$', views.destroy),
]
