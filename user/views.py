from django.shortcuts import HttpResponse
from general.utils import auth


def user_profile(request):
    auth(request)
    return HttpResponse('User profile')

