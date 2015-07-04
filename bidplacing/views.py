from django.template import loader, RequestContext
from django.http import HttpResponse
import datetime
# Create your views here.


def index(request):
    t = loader.get_template('../templates/bidplacing/index.html')
    c = RequestContext(request)
    return HttpResponse(t.render(c))


def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse(now)