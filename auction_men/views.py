__author__ = 'neuro'

from django.http import HttpResponse
from django.template import RequestContext, loader

import pprint as pp


def main_page(request):
    context = {}
    if 'message' in request.session:
        context['message'] = request.session['message']
        del request.session['message']

    if request.user.is_authenticated():
        context['user'] = request.user

    template = loader.get_template('index.html')

    return HttpResponse(template.render(context))
