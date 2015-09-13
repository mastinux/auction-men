from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.http.response import HttpResponseRedirect
from django.template import loader, RequestContext
from django.http import HttpResponse
from models import *
from forms import BidForm, ProductForm
from urllib import unquote
from django.contrib.auth.models import User
import pprint as pp
from django.shortcuts import render
from PIL import Image
from auction_men import settings
from os import path


def retrieve_basic_info(request):
    context = {}

    if 'message' in request.session:
        context['message'] = request.session['message']
        del request.session['message']

    if 'error' in request.session:
        context['error'] = request.session['error']
        del request.session['error']

    if request.user.is_authenticated():
        context['user'] = request.user

    top_categories = Category.get_top_categories()
    context['top_categories'] = top_categories

    #category_children = {}
    #for c in top_categories:
    #    category_children[c.id] = c.get_children_category()
    #context['category_children'] = category_children

    return context


def main_page(request):

    context = retrieve_basic_info(request)

    expiring_auctions = Product.get_unexpired_auctions(d=1)
    context['expiring_auctions'] = expiring_auctions.exclude(seller=request.user.id)

    last_insertions = Product.get_last_inserts(d=1)
    context['last_insertions'] = last_insertions.exclude(seller=request.user.id)

    if not request.user.is_authenticated():
        request.session['message'] = 'To bid register or log-in, please'
    else:
        suggested_products = Product.get_home_suggested_products(request.user)
        context['suggested_products'] = suggested_products

    context['form'] = BidForm()

    template = loader.get_template('index.html')

    context = RequestContext(request, context)

    return HttpResponse(template.render(context))


@login_required
def purchased_products_page(request):
    context = retrieve_basic_info(request)

    purchased_products = Product.get_recent_purchased_products(d=2)
    context['purchased_products'] = purchased_products

    purchase_bids = {}
    for p in purchased_products:
        purchase_bids[p.id] = Bid.objects.filter(product_name=p.id)\
            .order_by('-amount')[0]
    context['purchase_bids'] = purchase_bids

    template = loader.get_template('purchased_products.html')

    return HttpResponse(template.render(context))


@login_required
def user_purchased_products_page(request):
    context = retrieve_basic_info(request)

    purchased_products = Product.get_purchased_products(request.user.username)
    context['purchased_products'] = purchased_products

    purchase_bids = {}
    for p in purchased_products:
        purchase_bids[p.id] = Bid.objects.filter(product_name=p.id)\
            .order_by('-amount')[0]

    context['purchase_bids'] = purchase_bids

    template = loader.get_template('purchased_products.html')

    return HttpResponse(template.render(context))


@login_required
def selling_products_page(request):
    context = retrieve_basic_info(request)

    selling_products = Product.get_unexpired_user_products(
        request.user.username).order_by('deadline_time')
    context['selling_products'] = selling_products

    template = loader.get_template('selling_products.html')

    return HttpResponse(template.render(context))


def top_bids_page(request):
    context = retrieve_basic_info(request)

    unexpired_auctions = Product.objects.filter(deadline_time__gt=timezone.now())
    top_bids = Bid.objects.filter(product_name__in=[product.id for product in unexpired_auctions])\
                   .order_by('-amount')[:15]
    context['top_bids'] = top_bids

    template = loader.get_template('top_bids.html')

    return HttpResponse(template.render(context))


def contact_page(request):
    context = retrieve_basic_info(request)

    template = loader.get_template('contact.html')

    return HttpResponse(template.render(context))


def about_page(request):
    context = retrieve_basic_info(request)

    template = loader.get_template('about.html')

    return HttpResponse(template.render(context))


@login_required
def profile_page(request):
    context = retrieve_basic_info(request)

    context['user_bids'] = Bid.get_placed_bids(request.user.username)\
        .order_by('bidding_time')#[:10]

    context['selling_products'] = Product.get_user_products(request.user.username)\
        .order_by('-insertion_time')[:10]

    context['user_purchases'] = Product.get_purchased_products(
        request.user.username)

    template = loader.get_template('profile.html')

    context = RequestContext(request, context)

    return HttpResponse(template.render(context))


def category_page(request, cat_id):
    context = retrieve_basic_info(request)

    category_id = cat_id
    category_object = Category.objects.get(id=category_id)
    context['category'] = category_object

    category_products = category_object.get_category_product()
    context['category_products'] = category_products

    children_categories = {}
    children = category_object.get_children_category()

    for c in children:
        cat_id = c.id
        children_categories[cat_id] = c.get_category_product()
    context['children_categories'] = children_categories

    template = loader.get_template('category.html')

    context = RequestContext(request, context)

    return HttpResponse(template.render(context))


def product_page(request):
    context = retrieve_basic_info(request)

    product_id = unquote(request.get_full_path().split('/', 2)[2])
    product = Product.objects.get(id=product_id)
    context['product'] = product

    category = Category.objects.get(id=product.category_id)
    context['category'] = category

    seller = User.objects.get(username=product.seller)
    context['seller'] = seller

    seller_products = Product.objects.filter(seller=seller.id)
    context['seller_products'] = seller_products
    seller_bids = Bid.objects.filter(bidder=seller.id).__len__()
    context['seller_bids'] = seller_bids
    seller_purchases = Product.get_purchased_products(seller.username)
    context['seller_purchases'] = seller_purchases

    past_bids = product.get_past_bids()
    context['past_bids'] = past_bids

    past_sales = Product.get_expired_user_products(product.seller)
    context['past_sales'] = past_sales

    same_category_products = category.get_category_product()\
        .exclude(id=product.id)
    context['same_category_products'] = same_category_products

    template = loader.get_template('product.html')

    context = RequestContext(request, context)

    return HttpResponse(template.render(context))


@login_required
def place_bid(request, product_id):

    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        amount = request.POST['amount']
        bidder = request.user
        bid = Bid.create(product, bidder, amount)
        if float(bid.amount) <= product.get_best_bid():
            error = 'Could not bid an amount lower or equal than max bid'
            request.session['error'] = error
        else:
            request.session['message'] = 'You are the best bidder!!'
            bid.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def search_page(request):
    context = retrieve_basic_info(request)
    searched_value = request.GET['searched_value']

    if len(searched_value) > 2:
        context['searched_value'] = searched_value

        categories_found = Category.objects.filter(
            category_name__icontains=searched_value)
        context['categories_found'] = categories_found

        category_products_found = {}
        for category_found in categories_found:
            category_products = category_found.get_category_product()
            category_products_found[category_found.id] = category_products
        context['category_products_found'] = category_products_found

        products_found = Product.objects.filter(
            product_name__icontains=searched_value)
        context['products_found'] = products_found

    template = loader.get_template('search.html')
    context = RequestContext(request, context)

    return HttpResponse(template.render(context))


@login_required
def update_profile(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        user.first_name = request.POST['first_name'] or user.first_name
        user.last_name = request.POST['last_name'] or user.last_name
        user.save()
        request.user = user
    template = loader.get_template('profile.html')
    context = retrieve_basic_info(request)
    context = RequestContext(request, context)

    return HttpResponseRedirect('/accounts/profile')


@login_required
def new_product(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProductForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            product = form.save(commit=False)
            product.seller = request.user
            product.save()

            # redirect to a new URL:
            request.session['message'] = 'Product successfully added'
            return HttpResponseRedirect('/')
    # if a GET (or any other method) we'll create a blank form
    else:
        context = retrieve_basic_info(request)
        form = ProductForm()
        context['form'] = form
        return render(request, 'new_product.html', context)

    return render(request, 'new_product.html', {'form': form})


def show_product(request, product_id):
    context = retrieve_basic_info(request)

    product = Product.objects.get(id=product_id)
    context['product'] = product

    category = Category.objects.get(id=product.category_id)
    context['category'] = product.category

    seller = User.objects.get(username=product.seller)
    context['seller'] = product.seller

    seller_bids = Bid.objects.filter(bidder=seller.id).__len__()
    context['seller_bids'] = seller_bids
    seller_purchases = Product.get_purchased_products(seller.username).__len__()
    context['seller_purchases'] = seller_purchases
    seller_products = Product.objects.filter(seller=seller.id).__len__()
    context['seller_products'] = seller_products

    past_bids = product.get_past_bids()
    context['past_bids'] = past_bids

    past_sales = Product.get_expired_user_products(product.seller)
    context['past_sales'] = past_sales

    same_category_products = category.get_category_product().exclude(
        id=product.id)
    context['same_category_products'] = same_category_products.exclude(seller=request.user.id)

    if request.user.is_authenticated():
        suggested_products = Product.get_product_suggested_products(request.user.id, product.id)
        context['suggested_products'] = suggested_products

    template = loader.get_template('product.html')
    context = RequestContext(request, context)
    return HttpResponse(template.render(context))
