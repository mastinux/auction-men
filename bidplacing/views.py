from django.template import loader, RequestContext, response
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

    top_categories = Category.get_top_categories()
    category_list = list([category.category_name for category in top_categories])
    context['top_categories'] = category_list

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

    #get Books from /category/Books
    category = unquote(request.get_full_path().split('/', 2)[2])[:-1]
    context['category'] = Category.objects.get(category_name=category)

    template = loader.get_template('category.html')

    return HttpResponse(template.render(context))