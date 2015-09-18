from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout


def login_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    template = loader.get_template('login.html')
    return HttpResponse(template.render())


def register_page(request):

    if request.user.is_authenticated():
        return HttpResponseRedirect('/')

    template = loader.get_template('register.html')
    form = UserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            new_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, new_user)

            # message saved in session because in that way message can be used
            # from the view after redirect (HttpResponseRedirect don't allow
            # to pass parameters)
            request.session['message'] = 'Thanks for subscribing'
            return HttpResponseRedirect('/')
    else:
        context = {'form': form}
        context = RequestContext(request, context)
        return HttpResponse(template.render(context))


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
