from django.shortcuts import HttpResponse, loader, HttpResponseRedirect
from general.utils import auth, get_username
from general.models import User


def user_profile(request):
    if auth(request):
        template = loader.get_template('user/user_page.html')
        context = {
            'user': User.objects.filter(username=get_username(request))[0]
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect("/denied")
