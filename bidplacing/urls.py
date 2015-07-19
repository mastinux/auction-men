__author__ = 'mastinux'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.user_profile, name='user_profile')
]