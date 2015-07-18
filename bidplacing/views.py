from django.template import loader, RequestContext
from django.http import HttpResponse
import datetime
# Create your views here.


def main_page(request, message={}):
    context = {}
    if request.user.is_authenticated():
        context['user'] = request.user
    context['message'] = message
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))