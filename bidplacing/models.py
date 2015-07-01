from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AuctionsUser(models.Model):
    user = models.ForeignKey(User)
    # TODO integrare direttamente gli attributi di User
    # per evitare creazione della tabella auth_user

    def __init__(self, user):
        self.user = user
    # TODO problemi nel salvare da django shell:
    # object has no attribute '_state'

    def __unicode__(self):
        return self.user.username


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self', null=True)
    level = models.IntegerField(default=0)

    def __init__(self, category_name, parent=None, level=0):
        self.category_name = category_name
        self.parent = parent
        self.level = level

    def __unicode__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    start_price = models.FloatField()
    deadline_time = models.DateTimeField('deadline time')
    seller = models.ForeignKey(AuctionsUser)
    category = models.ForeignKey(Category)

    def __init__(self, product_name, description, start_price,
                 deadline_time, seller, category):
        self.product_name = product_name
        self.description = description
        self.start_price = start_price
        self.deadline_time = deadline_time
        self.seller = seller
        self.category = category

    def __unicode__(self):
        return self.product_name


class Bid(models.Model):
    product_name = models.OneToOneField(Product)
    bidder = models.ForeignKey(AuctionsUser)
    amount = models.FloatField()
    bidding_time = models.DateTimeField('bidding time')

    def __init__(self, product_name, bidder, amount,
                 bidding_time):
        self.product_name = product_name
        self.bidder = bidder
        self.amount = amount
        self.bidding_time = bidding_time

    def __unicode__(self):
        return self.product_name, self.bidder, self.amount