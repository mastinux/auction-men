from django.contrib import admin
from .models import *
# Register your models here.


class AuctionsUserAdmin(admin.ModelAdmin):
    fields = ['user']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['category_name', 'parent', 'level']
    list_display = ['category_name', 'parent', 'is_top_category']
    search_fields = ['category_name']


class ProductAdmin(admin.ModelAdmin):
    fields = ['product_name', 'description', 'start_price',
              'deadline_time', 'seller', 'category']
    list_display = ['product_name', 'description', 'start_price',
                    'deadline_time', 'seller', 'category']
    list_filter = ('deadline_time',)
    date_hierarchy = 'deadline_time'


class ImageAdmin(admin.ModelAdmin):
    fields = ['product_name', 'image']


class BidAdmin(admin.ModelAdmin):
    fields = ['product_name', 'bidder', 'amount', 'bidding_time']
    list_display = ['product_name', 'bidder', 'amount', 'bidding_time']

admin.site.register(AuctionsUser, AuctionsUserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Bid, BidAdmin)
