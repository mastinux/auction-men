__author__ = 'mastinux'

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.main_page, name='user'),
    ###
    url(r'^contact', views.contact_page, name='contact_page'),
    url(r'^about', views.about_page, name='about_page'),
    url(r'^update-profile', views.update_profile, name='update_profile'),
    url(r'^new-product', views.new_product, name='new_product'),
]