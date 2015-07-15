from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

'''
class AuctionsUser(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.user.username

    def all(self):
        AuctionsUser.objects.all()
'''


# data source: http://www.amazon.com/gp/site-directory/ref=nav_shopall_btn
class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True, null=False)
    parent = models.ForeignKey('self', null=True, blank=True, default=None)
    level = models.IntegerField(default=0)

    def __unicode__(self):
        return self.category_name

    def is_top_category(self):
        if self.level == 0:
            return True
        else:
            return False


class Product(models.Model):
    product_name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True)
    start_price = models.FloatField()
    deadline_time = models.DateTimeField('deadline time')
    seller = models.ForeignKey(User)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.product_name

    @staticmethod
    def get_user_products(user):
        user_tmp = User.objects.get(username=user)
        return Product.objects.filter(seller=user_tmp)

    @staticmethod
    def get_ranged_products(start, end):
        return Product.objects.filter(start_price__gte=start).exclude(start_price__gt=end)

    @staticmethod
    def get_expiring_auctions(m=0, h=0, d=0):
        start_time = timezone.now()
        end_time = start_time + timedelta(minutes=m) + timedelta(hours=h) + timedelta(days=d)
        return Product.objects.filter(deadline_time__gt=start_time, deadline_time__lt=end_time)
# TODO continue adding new methods


# TODO continue developing image manager tools
# problems viewing all images by admin
class Image(models.Model):
    product_name = models.ForeignKey(Product)
    image = models.ImageField()

    def __unicode__(self):
        return self.product_name


class Bid(models.Model):
    product_name = models.OneToOneField(Product)
    bidder = models.ForeignKey(User)
    amount = models.FloatField()
    bidding_time = models.DateTimeField('bidding time')

    def __unicode__(self):
        return self.product_name, self.bidder, self.amount