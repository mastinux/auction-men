from django.contrib import admin
from models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    fields = ['category_name', 'parent', 'level']
    list_display = ['category_name', 'parent', 'is_top_category']
    search_fields = ['category_name']


class ProductAdmin(admin.ModelAdmin):
    fields = ['product_name', 'deadline_time', 'seller', 'start_price',
              'category']
    list_display = ['product_name', 'deadline_time', 'seller', 'start_price',
                    'best_bidder', 'best_bid', ]
    search_fields = ['product_name', ]
    list_filter = ('deadline_time',)

    def best_bid(self, obj):
        return obj.get_best_bid()
    best_bid.short_description = "current price"

    def best_bidder(self, obj):
        return obj.get_best_bidder()
    best_bidder.short_description = "best bidder"


class BidAdmin(admin.ModelAdmin):
    fields = ['product_name', 'bidder', 'amount']
    list_display = ['product_name', 'bidder', 'amount', 'bidding_time']
    search_fields = ['product_name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Bid, BidAdmin)