from django.shortcuts import loader, HttpResponse, HttpResponseRedirect
from general.models import Event, Movie, Theatre, User
from general.utils import auth, get_username


def event_detail(request, index):
    if not auth(request):
        return HttpResponseRedirect('/denied')
    event = Event.objects.get(pk=index)
    template = loader.get_template('event/event_detail.html')
    context = {
        'event':event
    }
    return HttpResponse(template.render(context, request))


def event_list(request):
    if not auth(request):
        return HttpResponseRedirect('/denied')
    uname = get_username(request)
    events = Event.objects.filter(users__username=uname)
    template = loader.get_template('event/event_list.html')
    context = {
        'events': events
    }
    return HttpResponse(template.render(context, request))


def create_event(request):
    if not auth(request):
        return HttpResponseRedirect('/denied')
    template = loader.get_template('event/create_event.html')
    context = {
        'movies': Movie.objects.all(),
        'theatres': Theatre.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def do_create(request):
    if not auth(request):
        return HttpResponseRedirect('/denied')
    event = Event()
    event.name = request.POST['name']
    #event.datetime = request.POST['datetime']
    event.theatre = Theatre.objects.get(pk=request.POST['theatre'])
    event.movie = Movie.objects.get(pk=request.POST['movie'])
    users = []
    for username in request.POST['users'].split(','):
        users.append(username)
    return HttpResponse('event created: %s <br />%s' % (event, users))
