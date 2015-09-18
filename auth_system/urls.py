__author__ = 'neuro'

from django.conf.urls import url
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    url(
        regex=r'^login/$',
        view=login,
        kwargs={'template_name': 'login.html'},
        name='login_page'
    ),

    url(r'^register', views.register_page, name='register_page'),

    url(r'^logout', views.logout_view, name='logout')
]
