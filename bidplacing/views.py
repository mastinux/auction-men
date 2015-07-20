from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from bidplacing.models import *
from urllib import unquote
# Create your views here.


def main_page(request):
    context = {}

    if 'message' in request.session:
        context['message'] = request.session['message']
        del request.session['message']

    if request.user.is_authenticated():
        context['user'] = request.user
# TODO : avoid redundancy for next 3 rows in all methods views
    top_categories = Category.get_top_categories()
    category_list = list([category.category_name for category in top_categories])
    context['top_categories'] = category_list

    expiring_auctions = Product.get_coming_auctions(d=1)
    last_insertions = Product.get_last_inserts(d=1)
# TODO : develop recommendations system
    suggested_products = None
    context['expiring_auctions'] = expiring_auctions
    context['last_insertions'] = last_insertions
    context['suggested_products'] = suggested_products

    template = loader.get_template('index.html')

    return HttpResponse(template.render(context))


def contact_page(request):
    context = {}

    if 'message' in request.session:
        context['message'] = request.session['message']
        del request.session['message']

    if request.user.is_authenticated():
        context['user'] = request.user

    top_categories = Category.get_top_categories()
    category_list = list([category.category_name for category in top_categories])
    context['top_categories'] = category_list

    template = loader.get_template('contact.html')

    return HttpResponse(template.render(context))


def about_page(request):
    context = {}

    if 'message' in request.session:
        context['message'] = request.session['message']
        del request.session['message']

    if request.user.is_authenticated():
        context['user'] = request.user

    top_categories = Category.get_top_categories()
    category_list = list([category.category_name for category in top_categories])
    context['top_categories'] = category_list

    template = loader.get_template('about.html')

    return HttpResponse(template.render(context))


@login_required
def profile_page(request):
    context = {}
    if 'message' in request.session:
        context['message'] = request.session['message']
        del request.session['message']

    if request.user.is_authenticated():
        context['user'] = request.user

    top_categories = Category.get_top_categories()
    category_list = list([category.category_name for category in top_categories])
    context['top_categories'] = category_list
    context['user_bids'] = Bid.get_placed_bids(request.user.username)
    context['user_selling'] = Product.get_user_products(request.user.username)
    template = loader.get_template('profile.html')

    return HttpResponse(template.render(context))


def category_page(request):
    context = {}
    if 'message' in request.session:
        context['message'] = request.session['message']
        del request.session['message']

    if request.user.is_authenticated():
        context['user'] = request.user

    top_categories = Category.get_top_categories()
    category_list = list([category.category_name for category in top_categories])
    context['top_categories'] = category_list

    category = unquote(request.get_full_path().split('/', 2)[2])[:-1]
    context['category'] = category

    category_products = Product.get_category_products(category)
    context['category_products'] = category_products

    template = loader.get_template('category.html')

    return HttpResponse(template.render(context))


def product_page(request):
    context = {}
    if 'message' in request.session:
        context['message'] = request.session['message']
        del request.session['message']

    if request.user.is_authenticated():
        context['user'] = request.user

    top_categories = Category.get_top_categories()
    category_list = list([category.category_name for category in top_categories])
    context['top_categories'] = category_list

    product_name = unquote(request.get_full_path().split('/', 2)[2])
    product = Product.objects.get(product_name=product_name)
    context['product'] = product

    seller = User.objects.get(username=product.seller)
    context['seller'] = seller

    past_bids = product.get_past_bids()
    context['past_bids'] = past_bids

    past_sales = Product.get_expired_user_products(product.seller)
    context['past_sales'] = past_sales

    template = loader.get_template('product.html')

    return HttpResponse(template.render(context))


def place_bid(request):
    context = {}

# TODO : code managing new bid for a product, redirecting to the same product page

    template = loader.get_template('product.html')

    return HttpResponse(template.render(context))