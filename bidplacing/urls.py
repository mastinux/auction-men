__author__ = 'mastinux'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^current_datetime', views.current_datetime, name='current_datetime'),
]