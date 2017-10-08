from login.models import Session
import random, datetime


def __generate_token__():
    token = ''
    for i in range(0, 50):
        char = chr(random.randrange(33, 126))
        token += char
    return token


def create_token(username):
    update_expired_sessions()
    try:
        fltr = Session.objects.filter(username=username)
        return fltr[0].client_token
    except IndexError:
        sesh = Session()
        sesh.username = username
        sesh.client_token = __generate_token__()
        sesh.max_age = 600
        sesh.creation_age = datetime.datetime.now().timestamp()
        sesh.save()
        return sesh


def get_username(client_token):
    update_expired_sessions()
    sesh = Session.objects.get(client_token=client_token)
    if sesh is not None:
        return sesh.username
    else:
        return None


def update_expired_sessions():
    for sesh in Session.objects.all():
        if sesh.max_age + sesh.creation_age > datetime.datetime.now().timestamp():
            sesh.delete()


def auth(request):
    print(request.get_signed_cookie('client_token'))
    return False