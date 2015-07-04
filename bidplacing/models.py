from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AuctionsUser(models.Model):
    user = models.ForeignKey(User, unique=True)
    # TODO integrare direttamente gli attributi di User
    # per evitare di avere la foreign key su Users

    def __unicode__(self):
        return self.user.username

    def all(self):
        AuctionsUser.objects.all()


# data source: http://www.amazon.com/gp/site-directory/ref=nav_shopall_btn
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True, null=False)
    parent = models.ForeignKey('self', null=True, blank=True, default=None)
    level = models.IntegerField(default=0)

    def __unicode__(self):
        return self.category_name

    def all(self):
        Category.objects.all()

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
    seller = models.ForeignKey(AuctionsUser)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.product_name

    def all(self):
        Product.objects.all()


# TODO continue developing image manager tools
# problems viewing all images by admin
class Image(models.Model):
    product_name = models.ForeignKey(Product)
    image = models.ImageField()

    def __unicode__(self):
        return self.product_name

    def all(self):
        Image.objects.all()


class Bid(models.Model):
    product_name = models.OneToOneField(Product)
    bidder = models.ForeignKey(AuctionsUser)
    amount = models.FloatField()
    bidding_time = models.DateTimeField('bidding time')

    def __unicode__(self):
        return self.product_name, self.bidder, self.amount

    def all(self):
        Bid.objects.all()