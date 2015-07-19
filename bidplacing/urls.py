__author__ = 'mastinux'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main_page, name='user'),
    ###
    url(r'^contact', views.contact_page, name='contact_page'),
    url(r'^about', views.about_page, name='about_page'),
]