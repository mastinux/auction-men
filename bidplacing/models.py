from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Max
from datetime import timedelta, datetime


# category data source: http://www.amazon.com/gp/site-directory/ref=nav_shopall_btn
class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True, null=False)
    parent = models.ForeignKey('self', null=True, blank=True, default=None)
    level = models.IntegerField(default=0)

    def __unicode__(self):
        string = "%s [parent:%s, level=%s]" % (self.category_name, self.parent, self.level)
        return string

    @staticmethod
    def get_top_categories():
        return Category.objects.filter(level=0)

    def is_top_category(self):
        if self.level == 0:
            return True
        else:
            return False

    def get_children_category(self):
        return Category.objects.filter(parent=self.id, level=self.level+1)

    def get_category_product(self):
        return Product.objects.filter(category_id=self.id, deadline_time__gt=timezone.now())


class Product(models.Model):
    # TODO : add a field to know if product is a product or a service
    product_name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True)
    start_price = models.FloatField()
    insertion_time = models.DateTimeField(auto_now_add=True, blank=True)
    deadline_time = models.DateTimeField('deadline time')
    seller = models.ForeignKey(User)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        string = "%s [start_price=%s deadline=%s seller=%s]" % \
                 (self.product_name, self.start_price, self.deadline_time, self.seller)
        return string

    def save(self, *args, **kwargs):
        if self.deadline_time.__le__(timezone.now()):
            raise ValueError("Deadline_time could not be before now")
        if self.start_price < 0:
            raise ValueError("Start_price could not be negative")
        super(Product, self).save(*args, **kwargs)

    def get_remaining_time(self):
        return self.deadline_time - timezone.now()

    @staticmethod
    def get_user_products(user):
        user_tmp = User.objects.get(username=user)
        return Product.objects.filter(seller=user_tmp)

    @staticmethod
    def get_expired_user_products(user):
        user_tmp = User.objects.get(username=user)
        return Product.objects.filter(seller=user_tmp, deadline_time__lt=timezone.now())

    @staticmethod
    def get_coming_user_products(user):
        user_tmp = User.objects.get(username=user)
        return Product.objects.filter(seller=user_tmp).exclude(deadline_time__lt=timezone.now())

    @staticmethod
    def get_ranged_products(start, end):
        return Product.objects.filter(start_price__gte=start).exclude(start_price__gt=end)

    @staticmethod
    def get_coming_auctions(m=0, h=0, d=0):
        start_time = timezone.now()
        end_time = start_time + timedelta(minutes=m) + timedelta(hours=h) + timedelta(days=d)
        return Product.objects.filter(deadline_time__gt=start_time, deadline_time__lt=end_time)

    @staticmethod
    def get_last_inserts(m=0, h=0, d=0):
        start_time = timezone.now() - timedelta(minutes=m) - timedelta(hours=h) - timedelta(days=d)
        return Product.objects.filter(insertion_time__gt=start_time)

    @staticmethod
    def get_last_inserts_expired(m=0, h=0, d=0):
        return Product.get_last_inserts(m, h, d).filter(deadline_time__lt=timezone.now())

    @staticmethod
    def get_last_inserts_coming(m=0, h=0, d=0):
        return Product.get_last_inserts(m, h, d).filter(deadline_time__gt=timezone.now())

# TODO : delete because implemented by Bid.get_category_product
#    @staticmethod
#    def get_category_products(category_name):
#        category = Category.objects.get(category_name=category_name)
#        return Product.objects.filter(category__exact=category)

    def get_past_bids(self):
        return Bid.objects.filter(product_name=self.id).order_by('bidding_time')

    def get_best_bid(self):
        product = Product.objects.get(product_name=self.product_name,
                                      deadline_time=self.deadline_time, seller=self.seller)
        max_bid = product.bid_set.all().aggregate(Max('amount'))
        # it doesn't matter whose is the best bid because we call the method on a product object
        return max_bid.get('amount__max')


class Bid(models.Model):
    product_name = models.ForeignKey(Product)
    bidder = models.ForeignKey(User)
    amount = models.FloatField()
    bidding_time = models.DateTimeField(auto_now_add=True, blank=True)

    def __unicode__(self):
        string = "%s bidder=%s amount=%s bidding_time=%s" % \
                 (self.product_name, self.bidder, self.amount, self.bidding_time)
        return string

    def save(self, *args, **kwargs):
        if self.amount < 0:
            raise ValueError("Amount could not be negative")
        if timezone.now().__gt__(self.product_name.deadline_time):
            raise ValueError("Could not bid on an expired auction")
        if self.amount < self.product_name.get_best_bid():
            raise ValueError(
                "Could not bid an amount lower than max bid(%s) for the product"
                % self.product_name.get_best_bid())
        super(Bid, self).save(*args, **kwargs)

    @staticmethod
    def get_placed_bids(username):
        user = User.objects.get(username=username)
        return Bid.objects.filter(bidder=user)

    @staticmethod
    def get_expired_placed_bids(username):
        bidder = User.objects.get(username=username)
        return Bid.objects.filter(
            product_name__deadline_time__lt=timezone.now(), bidder=bidder)

    @staticmethod
    def get_coming_placed_bids(username):
        bidder = User.objects.get(username=username)
        return Bid.objects.filter(
            product_name__deadline_time__gt=timezone.now(), bidder=bidder)