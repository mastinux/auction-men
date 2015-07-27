from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Max, Min, Count, F
from datetime import timedelta, datetime, time


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
        return Category.objects.filter(level=0).order_by('category_name')

    def is_top_category(self):
        if self.level == 0:
            return True
        else:
            return False

    def get_children_category(self):
        return Category.objects.filter(parent=self.id, level=self.level + 1)

    def get_category_product(self):
        return Product.objects.filter(category_id=self.id, deadline_time__gt=timezone.now()).order_by('deadline_time')


class Product(models.Model):
    # TODO : add a field to know if product is a product or a service
    product_name = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=500, blank=True)
    start_price = models.FloatField()
    insertion_time = models.DateTimeField(auto_now_add=True, blank=True)
    deadline_time = models.DateTimeField('deadline time')
    seller = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    product_picture = models.ImageField(upload_to='',
                                        default='no-img.jpg')

    @property
    def best_bid(self):
        return self.get_best_bid()

    def __unicode__(self):
        string = "%s [start_price=%s deadline=%s seller=%s]" % \
                 (self.product_name, self.start_price, self.deadline_time, self.seller)
        return string

    def save(self, *args, **kwargs):
        if self.deadline_time.__le__(timezone.now()):
            raise ValueError("Deadline_time could not be before now")
        if self.start_price < 0:
            raise ValueError("Start_price could not be negative")
        hour = datetime.today().hour
        m = datetime.today().minute
        self.deadline_time = datetime.combine(
            self.deadline_time, time(hour, m))
        super(Product, self).save(*args, **kwargs)

    def get_remaining_time(self):
        remaining_time = self.deadline_time - timezone.now()
        if remaining_time.days < 0 or remaining_time.seconds < 0:
            return None
        else:
            return remaining_time

    @staticmethod
    def get_user_products(user):
        user_tmp = User.objects.get(username=user)
        return Product.objects.filter(seller=user_tmp)

    @staticmethod
    def get_expired_user_products(user):
        user_tmp = User.objects.get(username=user)
        return Product.objects.filter(seller=user_tmp, deadline_time__lt=timezone.now())

    @staticmethod
    def get_unexpired_user_products(user):
        user_tmp = User.objects.get(username=user)
        return Product.objects.filter(seller=user_tmp).exclude(deadline_time__lt=timezone.now())

    @staticmethod
    def get_recent_purchased_products(m=0, h=0, d=0):
        start = timezone.now() - timedelta(minutes=m) - timedelta(hours=h) - timedelta(days=d)
        end = timezone.now()

        expired_auctions = Product.objects.filter(deadline_time__gt=start, deadline_time__lt=end)

        product_id_list = Bid.objects.values('product_name__id').distinct() \
            .filter(product_name__in=[product.id for product in expired_auctions])

        purchased_products = []
        for product_id in product_id_list:
            p_id = product_id.get('product_name__id')

            max_bid = Bid.objects.filter(product_name=p_id).order_by('-bidding_time')[0]
            purchased_products.append(max_bid.product_name)

        return purchased_products

    @staticmethod
    def get_purchased_products(user):
        user_tmp = User.objects.get(username=user)

        expired_auctions = Product.objects.filter(deadline_time__lt=timezone.now())

        product_id_list = Bid.objects.values('product_name__id').distinct() \
            .filter(product_name__in=[product.id for product in expired_auctions])

        purchased_products = []
        for product_id in product_id_list:
            p_id = product_id.get('product_name__id')

            max_bid = Bid.objects.filter(product_name=p_id).order_by('-bidding_time')[0]
            if max_bid.bidder == user_tmp:
                purchased_products.append(max_bid.product_name)

        return purchased_products

    @staticmethod
    def get_home_suggested_products(user):
        user_purchased_products = Product.get_purchased_products(user)

        category_list = Category.objects.filter(id__in=[p.category.id for p in user_purchased_products])

        suggested_products = []
        for c in category_list:
            suggested_products.append(c.get_category_product()[:4])

        if suggested_products.__len__() > 0:
            return suggested_products[0]
        else:
            return None

    @staticmethod
    def get_product_suggested_products(user, product_id):
        current_user = User.objects.get(username=user)
        current_product = Product.objects.get(id=product_id)

        product_bidder = Bid.objects.all().filter(product_name=product_id).values('bidder').distinct()

        suggested_products = set()
        for p in Bid.objects.all().filter(bidder__in=[p.get('bidder') for p in product_bidder])\
                .exclude(bidder=current_user):
            suggested_products.add(p.product_name)

        if current_product in suggested_products:
            suggested_products.remove(current_product)

        if suggested_products.__len__() > 0:
            return suggested_products
        else:
            return None

    @staticmethod
    def get_unexpired_ranged_products(start, end):
        return Product.objects.filter(deadline_time__gt=timezone.now()) \
            .filter(start_price__gte=start).exclude(start_price__gt=end)

    @staticmethod
    def get_unexpired_auctions(m=0, h=0, d=0):
        start_time = timezone.now() + timedelta(hours=2)
        end_time = start_time + timedelta(minutes=m) + timedelta(hours=h) + timedelta(days=d)
        return Product.objects.filter(deadline_time__gt=start_time, deadline_time__lt=end_time)

    @staticmethod
    def get_last_inserts(m=0, h=0, d=0):
        start_time = timezone.now() - timedelta(minutes=m) - timedelta(hours=h) - timedelta(days=d)
        return Product.objects.filter(insertion_time__gt=start_time, deadline_time__gt=timezone.now()) \
            .order_by('insertion_time').reverse()

    @staticmethod
    def get_last_inserts_expired(m=0, h=0, d=0):
        return Product.get_last_inserts(m, h, d).filter(deadline_time__lt=timezone.now()).order_by('insertion_time')

    @staticmethod
    def get_last_inserts_unexpired(m=0, h=0, d=0):
        return Product.get_last_inserts(m, h, d).filter(deadline_time__gt=timezone.now()).order_by('insertion_time')

    def get_past_bids(self):
        return Bid.objects.filter(product_name=self.id).order_by('bidding_time')

    def get_best_bid(self):
        product = Product.objects.get(product_name=self.product_name,
                                      deadline_time=self.deadline_time, seller=self.seller)
        max_bid = product.bid_set.all().aggregate(Max('amount'))
        if max_bid.get('amount__max') is None:
            return self.start_price
        else:
            return max_bid.get('amount__max')


class Bid(models.Model):
    product_name = models.ForeignKey(Product)
    bidder = models.ForeignKey(User)
    amount = models.FloatField()
    bidding_time = models.DateTimeField(auto_now_add=True, blank=True)

    @classmethod
    def create(cls, product_name, bidder, amount):
        bid = cls(product_name=product_name, bidder=bidder, amount=amount)
        # do something with the book
        return bid

    def __unicode__(self):
        string = "%s bidder=%s amount=%s bidding_time=%s" % \
                 (self.product_name, self.bidder, self.amount, self.bidding_time)
        return string

    def save(self, *args, **kwargs):
        if self.amount < 0:
            raise ValueError("Amount could not be negative")
        if timezone.now().__gt__(self.product_name.deadline_time):
            raise ValueError("Could not bid on an expired auction")
        if float(self.amount) <= self.product_name.get_best_bid():
            raise ValueError(
                "Could not bid an amount lower or equal than max bid(%s) for the product"
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
    def get_unexpired_placed_bids(username):
        bidder = User.objects.get(username=username)
        return Bid.objects.filter(
            product_name__deadline_time__gt=timezone.now(), bidder=bidder)
