from django.shortcuts import loader, HttpResponse, HttpResponseRedirect
from general.models import Event, Movie, Theatre, User
from general.utils import auth, get_username


def event_detail(request, index):
    if not auth(request):
        return HttpResponseRedirect('/denied')
    event = Event.objects.get(pk=index)
    template = loader.get_template('event/event_detail.html')
    context = {
        'event': event,
        'title': event.name,
    }
    return HttpResponse(template.render(context, request))


def event_list(request):
    if not auth(request):
        return HttpResponseRedirect('/denied')
    uname = get_username(request)
    events = Event.objects.filter(users__username=uname)
    template = loader.get_template('event/event_list.html')
    context = {
        'events': events,
        'title': 'Events',
    }
    return HttpResponse(template.render(context, request))


def create_event(request):
    if not auth(request):
        return HttpResponseRedirect('/denied')
    template = loader.get_template('event/create_event.html')
    context = {
        'movies': Movie.objects.all(),
        'theatres': Theatre.objects.all(),
        'title': 'Create Event',
    }
    return HttpResponse(template.render(context, request))


def do_create(request):
    if not auth(request):
        return HttpResponseRedirect('/denied')
    event = Event()
    event.name = request.POST['name']
    event.theatre = Theatre.objects.get(pk=request.POST['theatre'])
    event.movie = Movie.objects.get(pk=request.POST['movie'])
    event.datetime = event.movie.datetime
    users = []
    event.save()
    for username in request.POST['users'].replace(' ', '').replace('\r', '').replace('\n', '').split(','):
        users.append(username)
        event.add_user(User.objects.get(username=username))
    event.save()
    return HttpResponse('event created: %s <br />%s' % (event, users))


def do_delete(request):
    if not auth(request):
        return HttpResponseRedirect('/denied')
    pk = request.POST['event_pk']
    Event.objects.get(pk=pk).delete()
    return HttpResponseRedirect('/event')
