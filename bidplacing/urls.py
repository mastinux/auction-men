__author__ = 'mastinux'

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.main_page, name='user'),
    ###
    url(r'^contact', views.contact_page, name='contact_page'),

    url(r'^about', views.about_page, name='about_page'),

    url(r'^update-profile', views.update_profile, name='update_profile'),

    #url(r'^product/', 'bidplacing.views.product_page', name='product_page'),
    #url(r'^place-bid/', 'bidplacing.views.place_bid', name='place_bid'),
    url(r'^search/', views.search_page, name='search_page'),

    url(r'^category/(?P<cat_id>[0-9]+)/',
        views.category_page,
        name='show_category'
        ),

    url(r'^products/product/new-product', views.new_product, name='new_product'),
    url(r'^products/product/(?P<product_id>[0-9]+)/$',
        views.show_product,
        name='show_product'),
    url(r'^products/product/(?P<product_id>[0-9]+)/new-bid',
        views.place_bid,
        name='place_bid'),
    url(r'^top_bids',
        views.top_bids_page,
        name='top_bids_page'),
    url(r'^products/purchased_products',
        views.purchased_products_page,
        name='purchased_products_page'),
    url(r'^products/selling_products/',
        views.selling_products_page,
        name='selling_page')
]