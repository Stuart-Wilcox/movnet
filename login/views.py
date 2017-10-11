from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import loader
from general import utils
from general.models import User
from . models import Session


def login_form(request):
    template = loader.get_template('login/login.html')
    context = {}
    return HttpResponse(template.render(context, request))


def login_user(request):
    u = request.POST.get('username')
    p = request.POST.get('password')

    user_obj = User.objects.filter(username=u)
    if len(user_obj) > 0:
        user_obj = user_obj[0]
    else:
        user_obj = None

    if user_obj is None:
        return HttpResponse('No user exists with this name.')

    if user_obj.password != p:
        return HttpResponse('Incorrect password.')

    sesh = utils.create_token(u)
    client_token = sesh.client_token
    max_age = sesh.max_age
    resp = HttpResponseRedirect('/user')
    resp.set_signed_cookie('client_token', client_token, max_age=max_age)

    return resp


def logout_user(request):
    username = utils.get_username(request)
    Session.objects.filter(username=username).delete()
    template = loader.get_template('login/logout.html')
    context = {}
    resp = HttpResponse(template.render(context, request))
    resp.delete_cookie('client_token')

    return resp
