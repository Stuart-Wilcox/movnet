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
    if len(Session.objects.filter(username=username)) > 0:
        return Session.objects.get(username=username)
    sesh = Session()
    sesh.username = username
    sesh.client_token = __generate_token__()
    sesh.max_age = 600
    sesh.creation_age = int(datetime.datetime.now().timestamp())
    sesh.save()
    return sesh


def get_username(request):
    update_expired_sessions()
    client_token = request.get_signed_cookie('client_token')
    print('CLIENT TOKEN: %s' % client_token)
    sesh = Session.objects.filter(client_token=client_token)
    if sesh is not None:
        return sesh[0].username
    else:
        return None


def update_expired_sessions():
    for sesh in Session.objects.all():
        if (sesh.max_age + sesh.creation_age) < int(datetime.datetime.now().timestamp()):
            sesh.delete()


def auth(request):
    try:
        print(request.get_signed_cookie('client_token'))
        return True
    except KeyError:
        return False
