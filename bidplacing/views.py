from django.template import loader, RequestContext
from django.http import HttpResponse
import datetime
# Create your views here.


def user_profile(request):
    template = loader.get_template('index.html')
    context= {}
    return HttpResponse(template.render(context))