from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.forms import Form
from django.http.response import HttpResponseRedirect
from django.template import loader, RequestContext
from django.http import HttpResponse
from models import *
from forms import BidForm, ProductForm
from urllib import unquote
from django.contrib.auth.models import User, AbstractUser# Create your views here.
import pprint as pp


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
# TODO : solve direct category page for left bar using http://getbootstrap.com/components/#btn-dropdowns-split
    expiring_auctions = Product.get_coming_auctions(d=1)
    last_insertions = Product.get_last_inserts(d=1)
# TODO : develop recommendations system
    suggested_products = None
    context['expiring_auctions'] = expiring_auctions
    context['last_insertions'] = last_insertions
    context['suggested_products'] = suggested_products
    context['form'] = BidForm()

    template = loader.get_template('index.html')

    context = RequestContext(request, context)

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

    context['user_bids'] = Bid.get_placed_bids(request.user.username)
    context['user_selling'] = Product.get_user_products(request.user.username)
    template = loader.get_template('profile.html')

    context = RequestContext(request, context)

    return HttpResponse(template.render(context))


def category_page(request, cat_id):
    context = retrieve_basic_info(request)
    category_id = cat_id
    category_object = Category.objects.get(id=category_id)
    category_products = category_object.get_category_product()
    children = category_object.get_children_category()
    children_categories = {}
    context['category_products'] = category_products
    context['category'] = category_object

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

    # code for left information table
# TODO : the 3 following calls slow down the response of the page, optimize it
    seller_products = Product.get_user_products(seller.username).__len__()
    context['seller_products'] = seller_products
    seller_bids = Bid.objects.filter(bidder=seller.id).__len__()
    context['seller_bids'] = seller_bids
    # TODO : develop purchased products
    seller_purchases = 0
    context['seller_purchases'] = seller_purchases

    past_bids = product.get_past_bids()
    context['past_bids'] = past_bids

    past_sales = Product.get_expired_user_products(product.seller)
    context['past_sales'] = past_sales

    same_category_products = category.get_category_product().exclude(id=product.id)
    context['same_category_products'] = same_category_products

    template = loader.get_template('product.html')
    context = RequestContext(request, context)
    return HttpResponse(template.render(context))

@login_required
def place_bid(request, product_id):
    if request.method == 'POST':
        product = Product.get_product(product_id)
        amount = request.POST['amount']
        bidder = request.user
        bid = Bid.create(product, bidder, amount)
        if float(bid.amount) <= product.get_best_bid():
            request.session['error'] = 'Could not bid an amount lower or equal than max bid'
        else:
            request.session['message'] = 'You are the best bidder!!'
            bid.save()

    return HttpResponseRedirect('/')

def search_page(request):
    context = retrieve_basic_info(request)

    searched_value = request.REQUEST.get('searched_value')

    if searched_value:
        context['searched_value'] = searched_value

        categories_found = Category.objects.filter(category_name__icontains=searched_value)
        context['categories_found'] = categories_found

        category_products_found = {}
        for category_found in categories_found:
            category_products = category_found.get_category_product()
            category_products_found[category_found.id] = category_products
        context['category_products_found'] = category_products_found

        products_found = Product.objects.filter(product_name__icontains=searched_value)
        context['products_found'] = products_found

    template = loader.get_template('search.html')

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
    form = ProductForm(request.POST or None)

    if form.is_valid():
        product = form.save(commit=False)
        product.seller = request.user

        product.save()

        request.session['message'] = 'Product succesfully added'
        return HttpResponseRedirect('/')
    template = loader.get_template('new_product.html')
    context = retrieve_basic_info(request)
    context['form'] = form
    context = RequestContext(request, context)

    return HttpResponse(template.render(context))

def show_product(request, product_id):
    context = retrieve_basic_info(request)

    product = Product.objects.get(id=product_id)
    category = Category.objects.get(id=product.category_id)
    seller = User.objects.get(username=product.seller)
    context['product'] = product
    context['category'] = product.category


    context['seller'] = product.seller

    seller_bids = Bid.objects.filter(bidder=seller.id).__len__()
    context['seller_bids'] = seller_bids
    # TODO : develop purchased products
    seller_purchases = 0
    context['seller_purchases'] = seller_purchases

    past_bids = product.get_past_bids()
    context['past_bids'] = past_bids

    past_sales = Product.get_expired_user_products(product.seller)
    context['past_sales'] = past_sales

    same_category_products = category.get_category_product().exclude(id=product.id)
    context['same_category_products'] = same_category_products

    template = loader.get_template('product.html')
    context = RequestContext(request, context)
    return HttpResponse(template.render(context))
