from django.http import HttpResponse
from django.shortcuts import loader
from general import utils
from general.models import User


def login_form(request):
    template = loader.get_template('login/login.html')
    context = {}
    return HttpResponse(template.render(context, request))


def login_user(request):
    u = request.POST.get('username')
    p = request.POST.get('password')
    print(p)
    print(u)

    user_obj = User.objects.filter(username=u)[0]

    print(user_obj)

    if user_obj is None:
        return HttpResponse('No user exists with this name.')

    if user_obj.password != p:
        return HttpResponse('Incorrect password.')

    sesh = utils.create_token(u)
    client_token = sesh.client_token
    max_age = sesh.max_age
    resp = HttpResponse('Successful login.')
    resp.set_signed_cookie('client_token', client_token, max_age=max_age)

    return resp
