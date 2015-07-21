from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse
from bidplacing.models import *
from urllib import unquote
# Create your views here.


def retrieve_basic_info(request):
    context = {}

    if 'message' in request.session:
        context['message'] = request.session['message']
        del request.session['message']

    if request.user.is_authenticated():
        context['user'] = request.user

    top_categories = Category.get_top_categories()
    top_category_list = {}
    category_children_list = {}
    for c in top_categories:
        top_category_list[c.id] = c.category_name
        category_children_list[c.id] = c.get_children_category()

    context['top_categories'] = top_category_list
    context['category_children_list'] = category_children_list

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

    template = loader.get_template('index.html')

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

    return HttpResponse(template.render(context))


def category_page(request):
    context = retrieve_basic_info(request)

    category_id = unquote(request.get_full_path().split('/', 2)[2])

    category_object = Category.objects.get(id=category_id)

    context['category'] = category_object.category_name

    category_products = category_object.get_category_product()
    context['category_products'] = category_products

    children = category_object.get_children_category()
    children_categories = {}
    for c in children:
        cat_id = c.id
        children_categories[cat_id] = c.get_category_product()
    context['children_categories'] = children_categories

    template = loader.get_template('category.html')

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

    return HttpResponse(template.render(context))


def place_bid(request):
    context = {}

# TODO : code managing new bid for a product, redirecting to the same product page

    template = loader.get_template('product.html')

    return HttpResponse(template.render(context))